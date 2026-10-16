# Ejemplos de Uso del Descargador de Blog

## Uso Básico

### 1. Descargar una entrada simple

```bash
./descargar_blog.sh 'https://tu-blog.com/entrada.html'
```

Esto creará una carpeta con el nombre del título de la entrada.

### 2. Descargar con nombre personalizado

```bash
./descargar_blog.sh 'https://tu-blog.com/entrada.html' 'mi-entrada'
```

Crea una carpeta llamada `mi-entrada/` con el contenido.

## Descargar Múltiples Entradas

### Script para descargar varias entradas a la vez

Crea un archivo llamado `descargar_multiples.sh`:

```bash
#!/bin/bash

# Lista de URLs de tu blog
entradas=(
    "https://facilitarelsoftwarelibre.blogspot.com/2023/11/entrada-1.html"
    "https://facilitarelsoftwarelibre.blogspot.com/2023/10/entrada-2.html"
    "https://facilitarelsoftwarelibre.blogspot.com/2023/09/entrada-3.html"
)

# Nombres personalizados (opcional)
nombres=(
    "entrada-1"
    "entrada-2"
    "entrada-3"
)

# Descargar cada entrada
for i in "${!entradas[@]}"; do
    echo "======================================="
    echo "Descargando entrada $((i+1))/${#entradas[@]}"
    echo "======================================="
    
    if [ ! -z "${nombres[$i]}" ]; then
        ./descargar_blog.sh "${entradas[$i]}" "${nombres[$i]}"
    else
        ./descargar_blog.sh "${entradas[$i]}"
    fi
    
    echo ""
    sleep 2  # Pausa de 2 segundos entre descargas
done

echo "✅ Todas las entradas descargadas!"
```

Luego ejecuta:

```bash
chmod +x descargar_multiples.sh
./descargar_multiples.sh
```

## Uso Directo con Python

Si prefieres usar Python directamente:

```bash
# Activar entorno virtual
source venv/bin/activate

# Descargar entrada
python3 blog_downloader.py 'URL' 'nombre-carpeta'

# Desactivar entorno virtual
deactivate
```

## Ejemplos Específicos para tu Blog

### Descargar entrada de KWallet (ya descargada)

```bash
./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html' 'kwallet-tutorial'
```

### Estructura resultante

```
kwallet-tutorial/
├── README.md
└── images/
    ├── image_001.webp
    ├── image_002.png
    ├── image_003.png
    └── ...
```

## Consejos Útiles

### 1. Organizar descargas por categoría

```bash
# Crear carpetas por categoría
mkdir -p descargas/tutoriales
mkdir -p descargas/guias
mkdir -p descargas/articulos

# Descargar en categorías
./descargar_blog.sh 'URL' 'descargas/tutoriales/entrada-1'
./descargar_blog.sh 'URL' 'descargas/guias/entrada-2'
```

### 2. Descargar con fecha

```bash
fecha=$(date +%Y-%m-%d)
./descargar_blog.sh 'URL' "${fecha}-nombre-entrada"
```

### 3. Lista desde archivo

Crea un archivo `urls.txt`:

```
https://tu-blog.com/entrada-1.html
https://tu-blog.com/entrada-2.html
https://tu-blog.com/entrada-3.html
```

Y usa este script:

```bash
#!/bin/bash
while IFS= read -r url; do
    echo "Descargando: $url"
    ./descargar_blog.sh "$url"
    sleep 2
done < urls.txt
```

## Verificar Descargas

### Ver contenido descargado

```bash
# Listar todas las carpetas descargadas
ls -la

# Ver contenido de una carpeta específica
ls -la kwallet-configuracion/
ls -la kwallet-configuracion/images/

# Ver el markdown en terminal
cat kwallet-configuracion/README.md | less
```

### Ver imágenes descargadas

```bash
# Contar imágenes
ls kwallet-configuracion/images/ | wc -l

# Ver tamaños de imágenes
du -h kwallet-configuracion/images/*
```

## Editar el Markdown Descargado

Una vez descargado, puedes editar el archivo `README.md` con cualquier editor:

```bash
# Con nano
nano kwallet-configuracion/README.md

# Con vim
vim kwallet-configuracion/README.md

# Con VS Code
code kwallet-configuracion/README.md

# Con gedit
gedit kwallet-configuracion/README.md
```

## Publicar en GitHub

```bash
# Inicializar repositorio en la carpeta descargada
cd kwallet-configuracion
git init
git add .
git commit -m "Primera versión del tutorial de KWallet"

# Subir a GitHub
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

## Solución de Problemas Comunes

### Error: No se encuentra la URL

Verifica que la URL está correcta y accesible:

```bash
curl -I 'https://tu-blog.com/entrada.html'
```

### Las imágenes no se descargaron

Verifica los permisos:

```bash
ls -la kwallet-configuracion/images/
```

### Regenerar una descarga

```bash
# Eliminar carpeta y volver a descargar
rm -rf nombre-carpeta
./descargar_blog.sh 'URL' 'nombre-carpeta'
```

## Automatización con Cron

Para descargar automáticamente cada semana:

```bash
# Editar crontab
crontab -e

# Agregar línea (ejecutar cada lunes a las 2 AM)
0 2 * * 1 cd /ruta/a/tu/proyecto && ./descargar_blog.sh 'URL' >> /tmp/blog-download.log 2>&1
```
