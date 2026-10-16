#!/bin/bash
# Script simple para descargar entradas de blog

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Descargador de Entradas de Blog      ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Verificar si existe Python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado"
    exit 1
fi

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    source venv/bin/activate
    echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
    echo ""
fi

# Si no se proporciona URL, mostrar ayuda
if [ $# -eq 0 ]; then
    echo "Uso: ./descargar_blog.sh <URL> [nombre_carpeta]"
    echo ""
    echo "Ejemplos:"
    echo "  ./descargar_blog.sh 'https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html'"
    echo "  ./descargar_blog.sh 'https://tu-blog.com/entrada' 'mi-entrada'"
    echo ""
    exit 1
fi

# Ejecutar el script de Python
python3 blog_downloader.py "$@"

exit $?
