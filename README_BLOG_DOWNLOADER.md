# Descargador de Entradas de Blog a Markdown

Script para descargar entradas de blog de Blogger (o cualquier sitio web) y convertirlas a formato Markdown, incluyendo todas las imágenes.

## Características

✅ Descarga el contenido completo de la entrada del blog
✅ Convierte HTML a Markdown limpio y legible  
✅ Descarga todas las imágenes de la entrada
✅ Organiza las imágenes en una carpeta separada
✅ Actualiza automáticamente las referencias a las imágenes en el Markdown
✅ Preserva el formato del texto (negritas, cursivas, enlaces, etc.)

## Requisitos

- Python 3.6 o superior
- pip3 (gestor de paquetes de Python)

## Instalación

### 1. Instalar dependencias

```bash
pip3 install -r requirements.txt
```

O manualmente:

```bash
pip3 install requests beautifulsoup4 html2text lxml
```

## Uso

### Opción 1: Usando el script bash (Recomendado)

```bash
./descargar_blog.sh 'URL_DE_TU_ENTRADA'
```

**Ejemplo con tu entrada de KWallet:**

```bash
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html'
```

**Con nombre de carpeta personalizado:**

```bash
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html' 'kwallet-tutorial'
```

### Opción 2: Usando Python directamente

```bash
python3 blog_downloader.py 'URL_DE_TU_ENTRADA'
```

**Con carpeta personalizada:**

```bash
python3 blog_downloader.py 'URL' 'nombre_carpeta'
```

## Estructura de salida

Después de ejecutar el script, se creará la siguiente estructura:

```
nombre-de-la-entrada/
├── README.md          # Contenido en Markdown
└── images/            # Carpeta con todas las imágenes
    ├── image_001.jpg
    ├── image_002.png
    └── ...
```

## Ejemplos de uso

### Descargar tu entrada de KWallet

```bash
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html'
```

### Descargar múltiples entradas

```bash
# Primera entrada
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/entrada-1.html' 'entrada-1'

# Segunda entrada  
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/entrada-2.html' 'entrada-2'

# Tercera entrada
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/entrada-3.html' 'entrada-3'
```

## Notas importantes

1. **URLs con caracteres especiales**: Siempre pon las URLs entre comillas simples
2. **Nombre de carpeta**: Si no especificas un nombre, se usará el título del post
3. **Imágenes**: Las imágenes se descargan con nombres secuenciales (image_001, image_002, etc.)
4. **Markdown**: El archivo generado se llama `README.md` para que sea fácil de visualizar en GitHub

## Solución de problemas

### Error: comando no encontrado

Si obtienes "comando no encontrado", asegúrate de:

```bash
chmod +x descargar_blog.sh
```

### Error: ModuleNotFoundError

Instala las dependencias:

```bash
pip3 install -r requirements.txt
```

### Error de conexión

- Verifica tu conexión a Internet
- Asegúrate de que la URL es correcta y accesible
- Algunas páginas pueden bloquear scripts automáticos

## Ventajas de este método

- 📝 Contenido portable en formato Markdown
- 🖼️ Imágenes guardadas localmente (no dependen del servidor original)
- 📁 Organización clara y fácil de gestionar
- 🔄 Reutilizable para múltiples entradas
- 🚀 Rápido y automatizado

## Personalización

Puedes modificar el archivo `blog_downloader.py` para:

- Cambiar el formato del nombre de las imágenes
- Ajustar el formato del Markdown generado
- Agregar metadatos adicionales
- Filtrar contenido específico

## Licencia

Este script es de uso libre para propósitos educativos y personales.
