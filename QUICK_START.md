# Quick Start Guide - Blog Post Downloader GUI

## 🚀 Inicio Rápido (Quick Start)

### En 3 pasos:

```bash
# 1. Dar permisos de ejecución
chmod +x run_gui.sh

# 2. Ejecutar la aplicación
./run_gui.sh

# 3. Usar la interfaz gráfica
# - Pegar URL del blog
# - Hacer clic en "Download Blog Post"
# - ¡Listo!
```

## 📋 Requisitos Previos

- Python 3.6+ (ya instalado ✓)
- Conexión a Internet

Todo lo demás se instala automáticamente.

## 🖥️ Capturas de Uso

### Paso 1: Ejecutar
```bash
./run_gui.sh
```

### Paso 2: Ingresar URL
Ejemplo:
```
https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html
```

### Paso 3: Configurar (Opcional)
- **Idioma**: English / Español
- **Carpeta**: Auto-crear o seleccionar manualmente

### Paso 4: Descargar
Clic en "Download Blog Post" / "Descargar Entrada del Blog"

## 📁 Resultado

```
tu-entrada-de-blog/
├── README.md          # ← Tu contenido en Markdown
└── images/            # ← Todas las imágenes
    ├── image_001.jpg
    ├── image_002.png
    └── ...
```

## 🌐 Cambiar Idioma

1. En la parte superior, selector "Language" / "Idioma"
2. Elegir: **English** o **Español**
3. La interfaz cambia inmediatamente

## ❓ Problemas Comunes

### "Permission denied"
```bash
chmod +x run_gui.sh
```

### "PyQt5 not found"
```bash
source venv/bin/activate
pip install PyQt5
python3 blog_downloader_gui.py
```

### La aplicación no abre
```bash
# Verificar Python
python3 --version

# Reinstalar dependencias
rm -rf venv
./run_gui.sh
```

## 💡 Tips

### ✅ Usar auto-crear carpeta
- Marca "Auto-create folder from post title"
- La app crea la carpeta automáticamente

### ✅ Ver progreso en tiempo real
- El área de log muestra todo el proceso
- Verás cuántas imágenes se descargan
- Mensajes de éxito o error

### ✅ Múltiples descargas
- Descarga una entrada
- Cambia la URL
- Descarga otra
- ¡Repite!

## 🎯 Casos de Uso

### Backup de tu blog
```
1. Abre la GUI
2. Copia URL de cada entrada
3. Descarga una por una
4. Tendrás todo tu blog en Markdown
```

### Migrar contenido
```
1. Descarga con la GUI
2. Los archivos Markdown están listos
3. Impórtalos a tu nuevo sistema
```

### Documentación offline
```
1. Descarga tutoriales importantes
2. Tendrás todo local
3. No necesitas Internet para leer
```

## 📚 Más Información

- **Manual completo**: Ver `README_GUI.md`
- **CLI version**: Ver `README_BLOG_DOWNLOADER.md`
- **Ejemplos**: Ver `EJEMPLOS_USO.md`

## 🆘 Soporte

Si algo no funciona:

1. Lee `README_GUI.md` (sección Solución de Problemas)
2. Verifica que Python 3 esté instalado
3. Ejecuta `./run_gui.sh` que instala todo automáticamente

## ✨ Características Principales

| Característica | Descripción |
|---------------|-------------|
| 🌐 Multiidioma | English & Español |
| 🖼️ Imágenes | Descarga automática |
| 📝 Markdown | Formato limpio |
| 👀 Progreso | Vista en tiempo real |
| 📁 Auto-carpetas | Basadas en título |
| ✅ Validación | URLs y rutas |

---

**¡Disfruta descargando tus entradas de blog!** 🎉
