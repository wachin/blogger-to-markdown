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
from datetime import datetime
from dateutil import parser as date_parser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QFileDialog, QProgressBar, QComboBox,
                             QGroupBox, QMessageBox, QCheckBox, QDialog)
from PyQt5.QtCore import QThread, pyqtSignal, QTranslator, QLocale, Qt, QUrl
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtSvg import QSvgWidget

class DownloadThread(QThread):
    """Thread for downloading blog posts without blocking the UI"""
    progress = pyqtSignal(str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, url, output_folder, add_date_prefix=False, date_format='YYYYMMDD'):
        super().__init__()
        self.url = url
        self.output_folder = output_folder
        self.add_date_prefix = add_date_prefix
        self.date_format = date_format
    
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
            
            # Extract publication date if enabled
            post_date = None
            if self.add_date_prefix:
                self.progress.emit(self.tr("Extracting publication date..."))
                post_date = extract_publication_date(soup, self.url)
                if post_date:
                    self.progress.emit(f"  ✓ {self.tr('Date found')}: {post_date.strftime('%Y-%m-%d')}")
                else:
                    self.progress.emit(f"  ⚠ {self.tr('Date not found, using current date')}")
                    post_date = datetime.now()
            
            # Determine output folder
            if self.output_folder and not self.add_date_prefix:
                # User specified folder
                final_folder = self.output_folder
            else:
                # Generate slug from title
                slug = generate_slug(title)
                
                # Use date prefix if enabled
                if self.add_date_prefix and post_date:
                    final_folder = format_date_folder_name(post_date, slug, self.date_format)
                else:
                    final_folder = slug
                
                # If user specified a base path, prepend it
                if self.output_folder:
                    final_folder = os.path.join(self.output_folder, final_folder)
            
            # Create output folder
            if not os.path.exists(final_folder):
                os.makedirs(final_folder)
            
            images_folder = os.path.join(final_folder, "images")
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
            markdown_filename = os.path.join(final_folder, "README.md")
            with open(markdown_filename, 'w', encoding='utf-8') as f:
                f.write(final_markdown)
            
            self.progress.emit(f"\n✅ {self.tr('Download completed!')}")
            self.progress.emit(f"📁 {self.tr('Files saved in')}: {final_folder}/")
            
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


def extract_publication_date(soup, url):
    """
    Extract publication date from post HTML or URL
    
    Args:
        soup: BeautifulSoup object of the HTML
        url: URL of the post
    
    Returns:
        datetime object or None if cannot be extracted
    """
    # Method 1: Search in meta tags
    meta_date = None
    
    # Blogger format
    meta_tags = [
        ('meta', {'property': 'article:published_time'}),
        ('meta', {'property': 'og:published_time'}),
        ('meta', {'name': 'date'}),
        ('meta', {'itemprop': 'datePublished'}),
    ]
    
    for tag_name, attrs in meta_tags:
        meta_tag = soup.find(tag_name, attrs)
        if meta_tag and meta_tag.get('content'):
            try:
                meta_date = date_parser.parse(meta_tag.get('content'))
                return meta_date
            except:
                pass
    
    # Method 2: Search in post content (Blogger specific)
    date_selectors = [
        ('span', 'date-header'),
        ('span', 'post-date'),
        ('time', 'published'),
        ('span', 'published'),
        ('abbr', 'published'),
        ('time', 'entry-date'),
    ]
    
    for tag, class_name in date_selectors:
        date_elem = soup.find(tag, class_=class_name)
        if date_elem:
            date_text = date_elem.get_text().strip()
            try:
                parsed_date = date_parser.parse(date_text, fuzzy=True)
                return parsed_date
            except:
                pass
    
    # Method 3: Extract from URL (Blogger format: /YYYY/MM/title.html)
    url_patterns = [
        r'/(\d{4})/(\d{2})/',  # /2023/11/
        r'(\d{4})-(\d{2})-(\d{2})',  # 2023-11-07
        r'/(\d{4})/(\d{2})/(\d{2})/',  # /2023/11/07/
    ]
    
    for pattern in url_patterns:
        match = re.search(pattern, url)
        if match:
            try:
                if len(match.groups()) == 2:
                    year, month = match.groups()
                    date_from_url = datetime(int(year), int(month), 1)
                else:
                    year, month, day = match.groups()
                    date_from_url = datetime(int(year), int(month), int(day))
                
                return date_from_url
            except:
                pass
    
    return None

def generate_slug(title):
    """
    Generate URL-friendly slug from title
    
    Args:
        title: Post title
    
    Returns:
        String slug in lowercase with hyphens
    """
    # Convert to lowercase
    slug = title.lower()
    
    # Replace common accented characters
    char_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ñ': 'n', 'ç': 'c',
    }
    
    for char, replacement in char_map.items():
        slug = slug.replace(char, replacement)
    
    # Replace non-alphanumeric characters with hyphens
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    
    # Replace spaces and multiple hyphens with single hyphen
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    
    # Remove leading and trailing hyphens
    slug = slug.strip('-')
    
    # Limit length
    if len(slug) > 100:
        slug = slug[:100].rstrip('-')
    
    return slug

def format_date_folder_name(date_obj, slug, date_format='YYYYMMDD'):
    """
    Format folder name with date and slug
    
    Args:
        date_obj: datetime object
        slug: String slug of title
        date_format: Date format ('YYYYMMDD', 'YYYY-MM-DD', etc.)
    
    Returns:
        String with formatted folder name
    """
    if not date_obj:
        return slug
    
    if date_format == 'YYYYMMDD':
        date_prefix = date_obj.strftime('%Y%m%d')
    elif date_format == 'YYYY-MM-DD':
        date_prefix = date_obj.strftime('%Y-%m-%d')
    else:
        date_prefix = date_obj.strftime('%Y%m%d')
    
    return f"{date_prefix}-{slug}"


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
        
        # Date prefix options
        date_group = QGroupBox(self.tr("Date-based Folder Naming"))
        date_layout = QVBoxLayout()
        
        self.add_date_checkbox = QCheckBox(self.tr("Add date prefix to folder name"))
        self.add_date_checkbox.setChecked(False)
        date_layout.addWidget(self.add_date_checkbox)
        
        # Date format selector
        date_format_layout = QHBoxLayout()
        date_format_label = QLabel(self.tr("Date format:"))
        self.date_format_combo = QComboBox()
        self.date_format_combo.addItem("YYYYMMDD (e.g., 20231107)", "YYYYMMDD")
        self.date_format_combo.addItem("YYYY-MM-DD (e.g., 2023-11-07)", "YYYY-MM-DD")
        date_format_layout.addWidget(date_format_label)
        date_format_layout.addWidget(self.date_format_combo)
        date_format_layout.addStretch()
        date_layout.addLayout(date_format_layout)
        
        date_group.setLayout(date_layout)
        input_layout.addWidget(date_group)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)
        
        # Buttons layout
        buttons_layout = QHBoxLayout()
        
        # Download button
        self.download_button = QPushButton(self.tr("Download Blog Post"))
        self.download_button.clicked.connect(self.start_download)
        self.download_button.setMinimumHeight(40)
        buttons_layout.addWidget(self.download_button)
        
        # About button
        self.about_button = QPushButton(self.tr("About"))
        self.about_button.clicked.connect(self.show_about)
        self.about_button.setMinimumHeight(40)
        self.about_button.setMaximumWidth(120)
        buttons_layout.addWidget(self.about_button)
        
        main_layout.addLayout(buttons_layout)
        
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
        
        # Get date-related options
        add_date_prefix = self.add_date_checkbox.isChecked()
        date_format = self.date_format_combo.currentData()
        
        # Clear log
        self.log_text.clear()
        
        # Disable download button
        self.download_button.setEnabled(False)
        self.statusBar().showMessage(self.tr("Downloading..."))
        
        # Start download thread
        self.download_thread = DownloadThread(
            url, 
            base_path if output_folder is None else output_folder,
            add_date_prefix=add_date_prefix,
            date_format=date_format
        )
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
    
    def show_about(self):
        """Show About dialog"""
        about_dialog = AboutDialog(self)
        about_dialog.exec_()


class AboutDialog(QDialog):
    """About dialog showing program information"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.tr("About Blog Downloader"))
        self.setMinimumSize(500, 400)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the dialog UI"""
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Left side - Icon
        icon_layout = QVBoxLayout()
        icon_layout.addStretch()
        
        # Load and display the icon
        icon_path = os.path.join(os.path.dirname(__file__), "icon.svg")
        if os.path.exists(icon_path):
            icon_widget = QSvgWidget(icon_path)
            icon_widget.setFixedSize(200, 200)
            icon_layout.addWidget(icon_widget, alignment=Qt.AlignCenter)
        else:
            # Fallback to default icon if SVG not found
            icon_label = QLabel("📝")
            icon_label.setStyleSheet("font-size: 120px;")
            icon_label.setAlignment(Qt.AlignCenter)
            icon_layout.addWidget(icon_label)
        
        icon_layout.addStretch()
        layout.addLayout(icon_layout)
        
        # Right side - Information
        info_layout = QVBoxLayout()
        
        # Program name and description
        title_label = QLabel("<h2>Blog Post Downloader</h2>")
        title_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(title_label)
        
        description = QLabel(
            self.tr("Tool to download blog posts and convert them to Markdown format with images. "
                   "Supports multiple blog platforms including Blogger.")
        )
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(description)
        
        info_layout.addSpacing(20)
        
        # Copyright
        copyright_label = QLabel("<b>Copyright:</b> © 2026 Washington Indacochea Delgado")
        info_layout.addWidget(copyright_label)
        
        # Email (clickable)
        email_label = QLabel('<b>Email:</b> <a href="mailto:linuxfrontier@proton.me">linuxfrontier@proton.me</a>')
        email_label.setOpenExternalLinks(True)
        info_layout.addWidget(email_label)
        
        # License
        license_label = QLabel("<b>License:</b> GPL3")
        info_layout.addWidget(license_label)
        
        # Website (clickable)
        website_label = QLabel('<b>Website:</b> <a href="https://github.com/wachin/blogger-to-markdown">https://github.com/wachin/blogger-to-markdown</a>')
        website_label.setOpenExternalLinks(True)
        info_layout.addWidget(website_label)
        
        info_layout.addSpacing(20)
        
        # Technologies used
        tech_title = QLabel("<b>Technologies Used:</b>")
        info_layout.addWidget(tech_title)
        
        tech_list = QLabel(
            "• Python 3\n"
            "• PyQt5\n"
            "• BeautifulSoup\n"
            "• html2text\n"
            "• requests"
        )
        info_layout.addWidget(tech_list)
        
        info_layout.addStretch()
        
        # Close button
        close_button = QPushButton(self.tr("Close"))
        close_button.clicked.connect(self.accept)
        info_layout.addWidget(close_button)
        
        layout.addLayout(info_layout)
    
    def tr(self, text):
        """Translation helper"""
        return QApplication.translate("AboutDialog", text)


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Blog Downloader")
    app.setOrganizationName("BlogTools")
    
    # Set application icon
    icon_path = os.path.join(os.path.dirname(__file__), "icon.svg")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
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
