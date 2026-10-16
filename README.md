![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey.svg)


# MDHoriZon Research - Project Repository

Este repositorio contiene múltiples proyectos de desarrollo web y herramientas.

## 📚 Proyectos Incluidos

### 1. 🌐 Clon de DigitalOcean
Recreación de la página principal de DigitalOcean con fines educativos.

**Archivos:**
- `index.html` - Estructura HTML
- `styles.css` - Estilos CSS responsive
- `script.js` - JavaScript con animaciones

**Para ver:** Abre `index.html` en tu navegador

---

### 2. 📝 Blog Post Downloader (CLI + GUI)

Herramienta para descargar entradas de blog a formato Markdown con imágenes.

#### 🖥️ Versión GUI (Recomendada)

**Características:**
- ✅ Interfaz gráfica moderna con PyQt5
- 🌐 Multiidioma (Inglés/Español)
- 👀 Progreso en tiempo real
- 📁 Auto-creación de carpetas
- 🖼️ Descarga automática de imágenes

**Inicio Rápido:**
```bash
./run_gui.sh
```

**Documentación completa:** Ver `README_GUI.md`

#### 💻 Versión CLI (Línea de Comandos)

**Para usuarios avanzados y scripts:**
```bash
./descargar_blog.sh 'URL_DEL_BLOG'
```

**Documentación completa:** Ver `README_BLOG_DOWNLOADER.md`

---

## 🚀 Inicio Rápido

### Blog Downloader GUI
```bash
# 1. Ejecutar (instala dependencias automáticamente)
./run_gui.sh

# 2. En la interfaz:
#    - Pegar URL del blog
#    - Seleccionar idioma (English/Español)
#    - Clic en "Download Blog Post"
```

### Blog Downloader CLI
```bash
# Usar directamente
./descargar_blog.sh 'https://tu-blog.com/entrada.html'

# O con carpeta personalizada
./descargar_blog.sh 'https://tu-blog.com/entrada.html' 'mi-carpeta'
```

---

## 📋 Requisitos

- Python 3.6 o superior
- pip3 (gestor de paquetes)
- Conexión a Internet

Las dependencias se instalan automáticamente.

---

## 📁 Estructura del Proyecto

```
MDHoriZon-research/
├── index.html                      # Landing page de DigitalOcean
├── styles.css                      # Estilos de la landing page
├── script.js                       # JavaScript de la landing page
│
├── blog_downloader_gui.py          # GUI con PyQt5
├── blog_downloader.py              # Script CLI
├── run_gui.sh                      # Ejecutar GUI
├── descargar_blog.sh              # Ejecutar CLI
│
├── translations/                   # Archivos de traducción
│   ├── blog_downloader_en.ts      # Inglés
│   └── blog_downloader_es.ts      # Español
│
├── kwallet-configuracion/          # Ejemplo de descarga
│   ├── README.md
│   └── images/
│
├── README.md                       # Este archivo
├── README_GUI.md                   # Documentación GUI
├── README_BLOG_DOWNLOADER.md      # Documentación CLI
├── QUICK_START.md                  # Guía rápida
├── EJEMPLOS_USO.md                 # Ejemplos de uso
└── requirements.txt                # Dependencias Python
```

---

## 🔧 Instalación Manual

Si prefieres instalar manualmente:

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar GUI
python3 blog_downloader_gui.py

# O ejecutar CLI
python3 blog_downloader.py 'URL'
```

---

## 🧪 Verificar Instalación

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar test
python3 test_gui.py
```

---

## 📖 Documentación Completa

- **Blog Downloader GUI:** `README_GUI.md`
- **Blog Downloader CLI:** `README_BLOG_DOWNLOADER.md`
- **Guía Rápida:** `QUICK_START.md`
- **Ejemplos de Uso:** `EJEMPLOS_USO.md`

---

## 🌐 Características del Blog Downloader

### Versión GUI
- Interfaz gráfica moderna
- Multiidioma (En/Es) con soporte i18n
- Selector de carpeta visual
- Progreso en tiempo real
- Validación de URLs
- Mensajes de error claros

### Versión CLI
- Scriptable y automatizable
- Múltiples descargas en lote
- Integración con pipelines
- Sin dependencias gráficas

### Ambas Versiones
- 📝 Conversión a Markdown limpio
- 🖼️ Descarga automática de imágenes
- 📁 Organización en carpetas
- 🔗 Enlaces actualizados
- ✅ Preserva formato

---

## 🎯 Casos de Uso

### Backup de Blog
```bash
./run_gui.sh
# Descargar cada entrada una por una
```

### Migración de Contenido
```bash
# Descargar todo el blog
for url in $(cat urls.txt); do
    ./descargar_blog.sh "$url"
done
```

### Documentación Offline
```bash
# Descargar tutoriales importantes
./run_gui.sh
# Y tendrás todo disponible sin Internet
```

---

## 💡 Tips y Trucos

### GUI
- Usa "Auto-create folder" para organización automática
- Cambia de idioma según tu preferencia
- El log muestra todo el proceso

### CLI
- Usa el script bash para instalación automática
- Crea scripts personalizados con `blog_downloader.py`
- Ver `EJEMPLOS_USO.md` para scripts avanzados

---

## ❓ Solución de Problemas

### Error: Permission denied
```bash
chmod +x run_gui.sh descargar_blog.sh
```

### Error: PyQt5 not found
```bash
source venv/bin/activate
pip install PyQt5
```

### La GUI no abre
```bash
# Reinstalar todo
rm -rf venv
./run_gui.sh
```

Ver documentación completa en `README_GUI.md` para más ayuda.

---

## 🤝 Contribuir

Mejoras bienvenidas:
- Nuevos idiomas para la GUI
- Soporte para más plataformas de blog
- Características adicionales

---

## 📄 Licencia

Proyectos educativos y de uso personal libre.

---

## 🎉 Ejemplo de Uso Exitoso

```bash
$ ./run_gui.sh

📦 Activando entorno virtual...
🚀 Iniciando aplicación...

# En la GUI:
# 1. Pegar URL del blog
# 2. Clic en "Download Blog Post"
# 3. ✅ ¡Descarga completada!

📁 Archivos guardados en: kwallet-configuracion/
   - README.md
   - images/ (13 imágenes)
```

---

**¡Disfruta de las herramientas!** 🚀
