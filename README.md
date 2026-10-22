![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey.svg)


# Blogger to Markdown

### 1. Blog Post Downloader (CLI + GUI)

Tool to download blog posts to Markdown format with images.

#### GUI Version (Recommended)

**Features:**
- Modern graphical interface with PyQt5
- Multilingual (English/Spanish)
- Real-time progress
- Auto-create folders
- Automatic image download

**Quick Start:**
```bash
./run_gui.sh
```

**Full documentation:** See `README_GUI.md`

#### CLI Version (Command Line)

**For advanced users and scripts:**
```bash
./descargar_blog.sh 'BLOG_URL'
```

**Full documentation:** See `README_BLOG_DOWNLOADER.md`

---

## Quick Start

### Blog Downloader GUI

```bash
./run_gui.sh
```

**Nota importante sobre `run_gui.sh`:**
- La primera vez puede tardar varios minutos en completarse, ya que instala automáticamente las dependencias necesarias (entorno virtual, PyQt5, etc.).
- Requiere que el paquete `python3-venv` esté instalado. Si no lo está, instalelo antes:
  ```bash
  sudo apt install python3-venv
  ```

### Blog Downloader CLI

```bash
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html'
```

---

## Requirements

- Python 3.6 or higher
- pip3 (package manager)
- Internet connection

---

## Debian/Ubuntu Installation (System Packages)

For Debian/Ubuntu users who prefer to use system packages instead of virtual environments:

### Install Required Packages

```bash
sudo apt install python3-venv python3-requests python3-html2text python3-bs4 python3-lxml python3-pyqt5 python3-dateutil
```

### Run the Program

Once the packages are installed, simply run:

```bash
# GUI version
python3 blog_downloader_gui.py

# CLI version
python3 blog_downloader.py 'URL'
```

---

## Manual Installation (with virtual environment)

Esta sección explica el proceso de instalacion manual utilizando un entorno virtual de Python.

```bash
# 1. Crear el entorno virtual (solo la primera vez)
python3 -m venv venv

# 2. Activar el entorno virtual (debe hacerse una sola vez por sesion de terminal)
source venv/bin/activate

# 3. Instalar dependencias (solo la primera vez o cuando requirements.txt cambie)
pip install -r requirements.txt

# 4. Ejecutar la interfaz grafica
python3 blog_downloader_gui.py

# 5. Para desactivar el entorno virtual cuando ya no lo necesite
deactivate
```

**Resumen del ciclo de vida del entorno virtual:**
1. `python3 -m venv venv` — Se ejecuta una sola vez para crear el entorno virtual.
2. `source venv/bin/activate` — Activa el entorno virtual. Debe hacerse una sola vez por cada nueva sesion de terminal.
3. `pip install -r requirements.txt` — Instala todas las dependencias del proyecto. Solo se necesita repetir si el archivo `requirements.txt` cambia.
4. `python3 blog_downloader_gui.py` — Lanza la interfaz grafica. Puede repetirse cuantas veces quiera mientras el entorno virtual esta activo.
5. `deactivate` — Desactiva el entorno virtual. Debe hacerse al terminar de usar el programa.

---

## Full Documentation

- **Blog Downloader GUI:** `README_GUI.md`
- **Blog Downloader CLI:** `README_BLOG_DOWNLOADER.md`
- **Quick Guide:** `QUICK_START.md`
- **Usage Examples:** `EJEMPLOS_USO.md`

---

## Blog Downloader Features

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
- Clean Markdown conversion
- Automatic image download
- Folder organization
- Updated links
- Format preservation
- **NEW:** Date-based folder names (YYYYMMDD-title)
- **NEW:** Automatic publication date extraction

---

## Use Cases

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

## Tips and Tricks

### GUI
- Use "Auto-create folder" for automatic organization
- Change language according to your preference
- The log shows the entire process

### CLI
- Use the bash script for automatic installation
- Create custom scripts with `blog_downloader.py`
- See `EJEMPLOS_USO.md` for advanced scripts

---

## Troubleshooting

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

## Contributing

Improvements welcome:
- New languages for GUI
- Support for more blog platforms
- Additional features

---

## License

Educational projects and free personal use.

---

## Successful Usage Example

```bash
$ ./run_gui.sh

Activando entorno virtual...
Iniciando aplicacion...

# In the GUI:
# 1. Paste blog URL
# 2. Click "Download Blog Post"
# 3. Descarga completada

Archivos guardados en: kwallet-configuracion/
   - README.md
   - images/ (13 images)
```

---

**Enjoy the tools!**
