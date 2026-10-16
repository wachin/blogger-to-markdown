#!/bin/bash
# Script para compilar archivos de traducción .ts a .qm

echo "🌐 Compilando archivos de traducción..."

# Buscar lrelease
LRELEASE=""
if command -v lrelease &> /dev/null; then
    LRELEASE="lrelease"
elif command -v lrelease-qt5 &> /dev/null; then
    LRELEASE="lrelease-qt5"
else
    echo "❌ Error: lrelease no encontrado"
    echo ""
    echo "Para instalar lrelease:"
    echo "  Ubuntu/Debian: sudo apt install qttools5-dev-tools"
    echo "  Fedora: sudo dnf install qt5-linguist"
    echo "  macOS: brew install qt5"
    echo ""
    exit 1
fi

# Compilar traducciones
echo "Usando: $LRELEASE"
echo ""

for ts_file in translations/*.ts; do
    if [ -f "$ts_file" ]; then
        qm_file="${ts_file%.ts}.qm"
        echo "📄 Compilando: $(basename $ts_file)"
        $LRELEASE "$ts_file" -qm "$qm_file"
        if [ $? -eq 0 ]; then
            echo "  ✓ Creado: $(basename $qm_file)"
        else
            echo "  ✗ Error al compilar $(basename $ts_file)"
        fi
        echo ""
    fi
done

echo "✅ Compilación completada"
