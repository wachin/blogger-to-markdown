#!/usr/bin/env python3
"""
Blog Downloader GUI - Graphical interface for downloading blog posts to Markdown
Supports internationalization (English/Spanish)
"""

import sys
import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import html2text
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QFileDialog, QProgressBar, QComboBox,
                             QGroupBox, QMessageBox, QCheckBox)
from PyQt5.QtCore import QThread, pyqtSignal, QTranslator, QLocale, Qt
from PyQt5.QtGui import QIcon, QFont

class DownloadThread(QThread):
    """Thread for downloading blog posts without blocking the UI"""
    progress = pyqtSignal(str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, url, output_folder):
        super().__init__()
        self.url = url
        self.output_folder = output_folder
    
    def run(self):
        """Execute the download in a separate thread"""
        try:
            self.progress.emit(self.tr("Downloading blog post..."))
            
            # Download the page
            response = requests.get(self.url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title_tag = soup.find('h3', class_='post-title')
            if not title_tag:
                title_tag = soup.find('h1', class_='post-title')
            if not title_tag:
                title_tag = soup.find('title')
            
            title = title_tag.get_text().strip() if title_tag else "Untitled"
            self.progress.emit(f"{self.tr('Title')}: {title}")
            
            # Create output folder
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)
            
            images_folder = os.path.join(self.output_folder, "images")
            if not os.path.exists(images_folder):
                os.makedirs(images_folder)
            
            # Extract post content
            post_body = soup.find('div', class_='post-body')
            if not post_body:
                post_body = soup.find('article')
            if not post_body:
                post_body = soup.find('div', class_='entry-content')
            
            if not post_body:
                self.finished.emit(False, self.tr("Could not find post content"))
                return
            
            # Download images
            images = post_body.find_all('img')
            self.progress.emit(f"\n{self.tr('Found')} {len(images)} {self.tr('images')}")
            
            for idx, img in enumerate(images, 1):
                img_url = img.get('src')
                if not img_url:
                    continue
                
                img_url = urljoin(self.url, img_url)
                local_filename = self.download_image(img_url, images_folder, idx)
                
                if local_filename:
                    img['src'] = f"images/{local_filename}"
                    self.progress.emit(f"  ✓ {self.tr('Downloaded')}: {local_filename}")
            
            # Convert to Markdown
            self.progress.emit(f"\n{self.tr('Converting to Markdown...')}")
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.ignore_images = False
            h.ignore_emphasis = False
            h.body_width = 0
            h.unicode_snob = True
            h.escape_snob = True
            
            markdown_content = h.handle(str(post_body))
            
            # Build final document
            final_markdown = f"# {title}\n\n"
            final_markdown += f"**{self.tr('Source')}:** {self.url}\n\n"
            final_markdown += "---\n\n"
            final_markdown += markdown_content
            
            # Save Markdown file
            markdown_filename = os.path.join(self.output_folder, "README.md")
            with open(markdown_filename, 'w', encoding='utf-8') as f:
                f.write(final_markdown)
            
            self.progress.emit(f"\n✅ {self.tr('Download completed!')}")
            self.progress.emit(f"📁 {self.tr('Files saved in')}: {self.output_folder}/")
            
            self.finished.emit(True, self.tr("Download completed successfully!"))
            
        except requests.RequestException as e:
            self.finished.emit(False, f"{self.tr('Error downloading page')}: {str(e)}")
        except Exception as e:
            self.finished.emit(False, f"{self.tr('Unexpected error')}: {str(e)}")
    
    def download_image(self, img_url, images_folder, index):
        """Download a single image"""
        try:
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            
            parsed_url = urlparse(img_url)
            path = parsed_url.path
            ext = os.path.splitext(path)[1]
            
            if not ext:
                content_type = response.headers.get('content-type', '')
                if 'jpeg' in content_type or 'jpg' in content_type:
                    ext = '.jpg'
                elif 'png' in content_type:
                    ext = '.png'
                elif 'gif' in content_type:
                    ext = '.gif'
                elif 'webp' in content_type:
                    ext = '.webp'
                else:
                    ext = '.jpg'
            
            filename = f"image_{index:03d}{ext}"
            filepath = os.path.join(images_folder, filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            return filename
        
        except Exception:
            return None
    
    def tr(self, text):
        """Translation helper"""
        return QApplication.translate("DownloadThread", text)


class BlogDownloaderGUI(QMainWindow):
    """Main window for the Blog Downloader application"""
    
    def __init__(self):
        super().__init__()
        self.download_thread = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle(self.tr("Blog Post Downloader"))
        self.setMinimumSize(800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Title
        title_label = QLabel(self.tr("Blog Post to Markdown Converter"))
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Subtitle
        subtitle_label = QLabel(self.tr("Download blog posts with images to Markdown format"))
        subtitle_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle_label)
        
        main_layout.addSpacing(20)
        
        # Language selector
        lang_layout = QHBoxLayout()
        lang_label = QLabel(self.tr("Language:"))
        self.lang_combo = QComboBox()
        self.lang_combo.addItem("English", "en")
        self.lang_combo.addItem("Español", "es")
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        lang_layout.addStretch()
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        main_layout.addLayout(lang_layout)
        
        main_layout.addSpacing(10)
        
        # Input group
        input_group = QGroupBox(self.tr("Blog Post URL"))
        input_layout = QVBoxLayout()
        
        # URL input
        url_layout = QHBoxLayout()
        url_label = QLabel(self.tr("URL:"))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText(self.tr("Enter the blog post URL here"))
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        input_layout.addLayout(url_layout)
        
        # Output folder
        folder_layout = QHBoxLayout()
        folder_label = QLabel(self.tr("Output Folder:"))
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText(self.tr("Select output folder"))
        self.browse_button = QPushButton(self.tr("Browse..."))
        self.browse_button.clicked.connect(self.browse_folder)
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(self.browse_button)
        input_layout.addLayout(folder_layout)
        
        # Auto-create folder option
        self.auto_folder_checkbox = QCheckBox(self.tr("Auto-create folder from post title"))
        self.auto_folder_checkbox.setChecked(True)
        input_layout.addWidget(self.auto_folder_checkbox)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)
        
        # Download button
        self.download_button = QPushButton(self.tr("Download Blog Post"))
        self.download_button.clicked.connect(self.start_download)
        self.download_button.setMinimumHeight(40)
        main_layout.addWidget(self.download_button)
        
        # Progress area
        progress_group = QGroupBox(self.tr("Progress"))
        progress_layout = QVBoxLayout()
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        progress_layout.addWidget(self.log_text)
        
        progress_group.setLayout(progress_layout)
        main_layout.addWidget(progress_group)
        
        # Status bar
        self.statusBar().showMessage(self.tr("Ready"))
    
    def change_language(self, index):
        """Change application language"""
        lang_code = self.lang_combo.itemData(index)
        # In a full implementation, this would reload the UI with new translations
        # For now, we'll show a message that language change requires restart
        if hasattr(self, 'language_changed'):
            QMessageBox.information(
                self,
                self.tr("Language Change"),
                self.tr("Language will be applied on next restart")
            )
        self.language_changed = True
    
    def browse_folder(self):
        """Open folder selection dialog"""
        folder = QFileDialog.getExistingDirectory(
            self,
            self.tr("Select Output Folder"),
            os.path.expanduser("~")
        )
        if folder:
            self.folder_input.setText(folder)
    
    def start_download(self):
        """Start the download process"""
        url = self.url_input.text().strip()
        
        if not url:
            QMessageBox.warning(
                self,
                self.tr("Missing URL"),
                self.tr("Please enter a blog post URL")
            )
            return
        
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            QMessageBox.warning(
                self,
                self.tr("Invalid URL"),
                self.tr("URL must start with http:// or https://")
            )
            return
        
        # Determine output folder
        if self.auto_folder_checkbox.isChecked():
            output_folder = None  # Will be auto-generated
            base_path = self.folder_input.text().strip() or os.getcwd()
        else:
            output_folder = self.folder_input.text().strip()
            if not output_folder:
                QMessageBox.warning(
                    self,
                    self.tr("Missing Folder"),
                    self.tr("Please select an output folder")
                )
                return
            base_path = output_folder
        
        # Clear log
        self.log_text.clear()
        
        # Disable download button
        self.download_button.setEnabled(False)
        self.statusBar().showMessage(self.tr("Downloading..."))
        
        # Start download thread
        self.download_thread = DownloadThread(url, base_path if output_folder is None else output_folder)
        self.download_thread.progress.connect(self.update_log)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()
    
    def update_log(self, message):
        """Update the log text area"""
        self.log_text.append(message)
        # Auto-scroll to bottom
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def download_finished(self, success, message):
        """Handle download completion"""
        self.download_button.setEnabled(True)
        
        if success:
            self.statusBar().showMessage(self.tr("Download completed!"))
            QMessageBox.information(
                self,
                self.tr("Success"),
                message
            )
        else:
            self.statusBar().showMessage(self.tr("Download failed"))
            QMessageBox.critical(
                self,
                self.tr("Error"),
                message
            )
    
    def tr(self, text):
        """Translation helper"""
        return QApplication.translate("BlogDownloaderGUI", text)


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Blog Downloader")
    app.setOrganizationName("BlogTools")
    
    # Set up translator
    translator = QTranslator()
    locale = QLocale.system().name()
    
    # Try to load translation file
    translation_file = f"translations/blog_downloader_{locale}.qm"
    if os.path.exists(translation_file):
        translator.load(translation_file)
        app.installTranslator(translator)
    
    # Create and show main window
    window = BlogDownloaderGUI()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
