#!/bin/bash
# Script para ejecutar la interfaz gráfica del descargador de blog

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Blog Post Downloader GUI              ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Verificar Python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado"
    exit 1
fi

# Activar o crear entorno virtual
if [ -d "venv" ]; then
    echo "📦 Activando entorno virtual..."
    source venv/bin/activate
else
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    source venv/bin/activate
    echo "📦 Instalando dependencias..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Verificar si PyQt5 está instalado
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  PyQt5 no está instalado. Instalando...${NC}"
    pip install PyQt5
fi

# Compilar traducciones si lrelease está disponible
if command -v lrelease &> /dev/null; then
    echo "🌐 Compilando traducciones..."
    lrelease translations/blog_downloader_en.ts -qm translations/blog_downloader_en.qm 2>/dev/null
    lrelease translations/blog_downloader_es.ts -qm translations/blog_downloader_es.qm 2>/dev/null
    echo "✓ Traducciones compiladas"
elif command -v lrelease-qt5 &> /dev/null; then
    echo "🌐 Compilando traducciones..."
    lrelease-qt5 translations/blog_downloader_en.ts -qm translations/blog_downloader_en.qm 2>/dev/null
    lrelease-qt5 translations/blog_downloader_es.ts -qm translations/blog_downloader_es.qm 2>/dev/null
    echo "✓ Traducciones compiladas"
else
    echo -e "${YELLOW}⚠️  lrelease no encontrado. Las traducciones pueden no funcionar.${NC}"
    echo "   Para compilar traducciones, instala: sudo apt install qttools5-dev-tools"
fi

echo ""
echo -e "${GREEN}🚀 Iniciando aplicación...${NC}"
echo ""

# Ejecutar la GUI
python3 blog_downloader_gui.py

exit_code=$?

# Desactivar entorno virtual
deactivate 2>/dev/null

exit $exit_code
