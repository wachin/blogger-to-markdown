# Blog Post Downloader - GUI Version

Interfaz gráfica para descargar entradas de blog a formato Markdown con soporte multiidioma (Inglés/Español).

## Características

✅ **Interfaz Gráfica Intuitiva** - Fácil de usar con PyQt5
✅ **Multiidioma** - Inglés y Español incluidos
✅ **Descarga Automática** - Descarga contenido e imágenes
✅ **Vista de Progreso** - Observa el progreso en tiempo real
✅ **Carpetas Automáticas** - Crea carpetas basadas en el título
✅ **Multiplataforma** - Funciona en Linux, Windows y macOS

## Captura de Pantalla

La aplicación incluye:
- Selector de idioma (Inglés/Español)
- Campo de entrada para URL del blog
- Selector de carpeta de salida
- Opción de auto-crear carpeta
- Área de progreso en tiempo real
- Mensajes de éxito/error

## Requisitos

- Python 3.6 o superior
- PyQt5
- Otras dependencias en `requirements.txt`

## Instalación

### Opción 1: Instalación Automática (Recomendada)

```bash
./run_gui.sh
```

Este script:
1. Crea el entorno virtual si no existe
2. Instala todas las dependencias automáticamente
3. Compila las traducciones
4. Inicia la aplicación

### Opción 2: Instalación Manual

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Compilar traducciones (opcional)
lrelease translations/blog_downloader_es.ts -qm translations/blog_downloader_es.qm

# Ejecutar aplicación
python3 blog_downloader_gui.py
```

## Uso

### 1. Iniciar la Aplicación

```bash
./run_gui.sh
```

### 2. Seleccionar Idioma

- Usa el selector de idioma en la parte superior
- Elige entre English o Español

### 3. Ingresar URL

- Pega la URL de la entrada del blog en el campo "URL"
- Ejemplo: `https://facilitarelsoftwarelibre.blogspot.com/2023/11/entrada.html`

### 4. Configurar Carpeta de Salida

**Opción A: Auto-crear carpeta (Recomendado)**
- Marca "Auto-create folder from post title"
- La carpeta se creará automáticamente con el título de la entrada

**Opción B: Seleccionar carpeta manualmente**
- Desmarca "Auto-create folder from post title"
- Haz clic en "Browse..." para seleccionar la carpeta

### 5. Descargar

- Haz clic en "Download Blog Post"
- Observa el progreso en el área de log
- Espera el mensaje de éxito

### 6. Resultado

La aplicación creará:
```
nombre-de-entrada/
├── README.md       # Contenido en Markdown
└── images/         # Todas las imágenes
    ├── image_001.jpg
    ├── image_002.png
    └── ...
```

## Idiomas Soportados

### English (Inglés)
- Idioma por defecto
- Interfaz completamente en inglés
- Mensajes de error y éxito en inglés

### Español
- Seleccionable desde el menú
- Interfaz completamente traducida
- Todos los mensajes en español

## Compilar Traducciones

Si necesitas recompilar las traducciones después de modificarlas:

### En Linux/macOS:

```bash
# Instalar herramientas de Qt (si no están instaladas)
sudo apt install qttools5-dev-tools  # Ubuntu/Debian
# o
brew install qt5  # macOS con Homebrew

# Compilar traducciones
lrelease translations/blog_downloader_es.ts -qm translations/blog_downloader_es.qm
lrelease translations/blog_downloader_en.ts -qm translations/blog_downloader_en.qm
```

### En Windows:

```cmd
# Asegúrate de tener Qt instalado
# Luego ejecuta:
lrelease translations\blog_downloader_es.ts -qm translations\blog_downloader_es.qm
lrelease translations\blog_downloader_en.ts -qm translations\blog_downloader_en.qm
```

## Agregar Nuevos Idiomas

### 1. Crear archivo de traducción

Copia `translations/blog_downloader_en.ts` y renómbralo, por ejemplo:
```bash
cp translations/blog_downloader_en.ts translations/blog_downloader_fr.ts
```

### 2. Editar traducciones

Abre el archivo `.ts` y traduce los textos:

```xml
<message>
    <source>Blog Post Downloader</source>
    <translation>Téléchargeur d'Articles de Blog</translation>
</message>
```

### 3. Compilar traducción

```bash
lrelease translations/blog_downloader_fr.ts -qm translations/blog_downloader_fr.qm
```

### 4. Agregar al selector de idioma

Edita `blog_downloader_gui.py` en la función `init_ui()`:

```python
self.lang_combo.addItem("Français", "fr")
```

## Estructura de Archivos

```
.
├── blog_downloader_gui.py          # Aplicación principal
├── run_gui.sh                      # Script de ejecución
├── requirements.txt                # Dependencias
├── translations/                   # Carpeta de traducciones
│   ├── blog_downloader_en.ts      # Traducción inglés (fuente)
│   ├── blog_downloader_es.ts      # Traducción español (fuente)
│   ├── blog_downloader_en.qm      # Compilado inglés
│   └── blog_downloader_es.qm      # Compilado español
└── README_GUI.md                   # Este archivo
```

## Solución de Problemas

### Error: "No module named 'PyQt5'"

```bash
source venv/bin/activate
pip install PyQt5
```

### Las traducciones no funcionan

1. Verifica que los archivos `.qm` existan en `translations/`
2. Recompila las traducciones:
```bash
lrelease translations/blog_downloader_es.ts -qm translations/blog_downloader_es.qm
```

### Error: "lrelease: command not found"

Instala las herramientas de Qt:
```bash
sudo apt install qttools5-dev-tools  # Ubuntu/Debian
```

### La aplicación no inicia

1. Verifica que Python 3 esté instalado: `python3 --version`
2. Activa el entorno virtual: `source venv/bin/activate`
3. Verifica las dependencias: `pip list | grep PyQt5`

### Permisos denegados

```bash
chmod +x run_gui.sh
./run_gui.sh
```

## Ventajas de la GUI

- 🖱️ **Más fácil de usar** que la línea de comandos
- 👀 **Vista en tiempo real** del progreso de descarga
- 🌐 **Multiidioma** - Fácil cambio de idioma
- ✅ **Validación automática** de URLs y rutas
- 📁 **Explorador de carpetas** integrado
- 💬 **Mensajes claros** de éxito y error

## Comparación: CLI vs GUI

| Característica | CLI (`blog_downloader.py`) | GUI (`blog_downloader_gui.py`) |
|----------------|---------------------------|--------------------------------|
| Facilidad de uso | Media | Alta |
| Progreso visible | Terminal | Interfaz gráfica |
| Selección de carpeta | Manual | Explorador de archivos |
| Multiidioma | No | Sí (En/Es) |
| Scriptable | Sí | No |
| Múltiples descargas | Sí (scripts) | Una a la vez |

## Licencia

Este software es de uso libre para propósitos educativos y personales.

## Contribuir

Para agregar nuevos idiomas o mejorar traducciones:

1. Edita los archivos `.ts` en `translations/`
2. Compila con `lrelease`
3. Prueba la aplicación
4. Comparte tus mejoras

## Soporte

Si encuentras algún problema:
1. Verifica los requisitos
2. Lee la sección de solución de problemas
3. Revisa los logs en el área de progreso de la aplicación
