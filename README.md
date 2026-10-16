![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey.svg)


# Blogger to Markdown

### 1. 📝 Blog Post Downloader (CLI + GUI)

Tool to download blog posts to Markdown format with images.

#### 🖥️ GUI Version (Recommended)

**Features:**
- ✅ Modern graphical interface with PyQt5
- 🌐 Multilingual (English/Spanish)
- 👀 Real-time progress
- 📁 Auto-create folders
- 🖼️ Automatic image download

**Quick Start:**
```bash
./run_gui.sh
```

**Full documentation:** See `README_GUI.md`

#### 💻 CLI Version (Command Line)

**For advanced users and scripts:**
```bash
./descargar_blog.sh 'BLOG_URL'
```

**Full documentation:** See `README_BLOG_DOWNLOADER.md`

---

## 🚀 Quick Start

### Blog Downloader GUI
```bash
# 1. Run (installs dependencies automatically)
./run_gui.sh

# 2. In the interface:
#    - Paste blog URL
#    - Select language (English/Español)
#    - Click "Download Blog Post"
```

### Blog Downloader CLI
```bash
# Use directly
./descargar_blog.sh 'https://your-blog.com/post.html'

# Or with custom folder
./descargar_blog.sh 'https://your-blog.com/post.html' 'my-folder'
```

---

## 📋 Requirements

- Python 3.6 or higher
- pip3 (package manager)
- Internet connection

Dependencies are installed automatically.

---

## � Debian/Ubuntu Installation (System Packages)

For Debian/Ubuntu users who prefer to use system packages instead of virtual environments:

### Install Required Packages

```bash
sudo apt install python3-requests python3-html2text python3-bs4 python3-lxml python3-pyqt5 python3-dateutil
```

### Run the Program

Once the packages are installed, simply run:

```bash
# GUI version
python3 blog_downloader_gui.py

# CLI version
python3 blog_downloader.py 'URL'
```

**Note:** This method is ideal for creating a .deb package for easy distribution on Debian-based systems.

---

## �🔧 Manual Installation

If you prefer to install manually:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run GUI
python3 blog_downloader_gui.py

# Or run CLI
python3 blog_downloader.py 'URL'
```

---

## 🧪 Verify Installation

```bash
# Activate virtual environment
source venv/bin/activate

# Run test
python3 test_gui.py
```

---

## 📖 Full Documentation

- **Blog Downloader GUI:** `README_GUI.md`
- **Blog Downloader CLI:** `README_BLOG_DOWNLOADER.md`
- **Quick Guide:** `QUICK_START.md`
- **Usage Examples:** `EJEMPLOS_USO.md`

---

## 🌐 Blog Downloader Features

### GUI Version
- Modern graphical interface
- Multilingual (En/Es) with i18n support
- Visual folder selector
- Real-time progress
- URL validation
- Clear error messages
- **NEW:** Date prefix option for folders
- **NEW:** Date format selector

### CLI Version
- Scriptable and automatable
- Multiple batch downloads
- Pipeline integration
- No graphical dependencies
- **NEW:** `--add-date` flag for date prefix
- **NEW:** `--date-format` option for date format

### Both Versions
- 📝 Clean Markdown conversion
- 🖼️ Automatic image download
- 📁 Folder organization
- 🔗 Updated links
- ✅ Format preservation
- **📅 NEW:** Date-based folder names (YYYYMMDD-title)
- **🔍 NEW:** Automatic publication date extraction

---

## 🎯 Use Cases

### Blog Backup with Dates
```bash
# With automatic date
./venv/bin/python3 blog_downloader.py 'https://your-blog.com/post.html' --add-date

# Result: 20231107-post-title/
```

### Blog Backup (Without dates)
```bash
./run_gui.sh
# Download each post one by one
```

### Content Migration
```bash
# Download entire blog
for url in $(cat urls.txt); do
    ./descargar_blog.sh "$url"
done
```

### Offline Documentation
```bash
# Download important tutorials
./run_gui.sh
# And you'll have everything available without Internet
```

---

## 💡 Tips and Tricks

### GUI
- Use "Auto-create folder" for automatic organization
- Change language according to your preference
- The log shows the entire process

### CLI
- Use the bash script for automatic installation
- Create custom scripts with `blog_downloader.py`
- See `EJEMPLOS_USO.md` for advanced scripts

---

## ❓ Troubleshooting

### Error: Permission denied
```bash
chmod +x run_gui.sh descargar_blog.sh
```

### Error: PyQt5 not found
```bash
source venv/bin/activate
pip install PyQt5
```

### GUI won't open
```bash
# Reinstall everything
rm -rf venv
./run_gui.sh
```

See full documentation in `README_GUI.md` for more help.

---

## 🤝 Contributing

Improvements welcome:
- New languages for GUI
- Support for more blog platforms
- Additional features

---

## 📄 License

Educational projects and free personal use.

---

## 🎉 Successful Usage Example

```bash
$ ./run_gui.sh

📦 Activating virtual environment...
🚀 Starting application...

# In the GUI:
# 1. Paste blog URL
# 2. Click "Download Blog Post"
# 3. ✅ Download completed!

📁 Files saved in: kwallet-configuracion/
   - README.md
   - images/ (13 images)
```

---

**Enjoy the tools!** 🚀
