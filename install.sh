#!/bin/bash

echo "🚀 Instalando Conversor RAR a ZIP..."
echo "======================================"

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor instálalo primero."
    echo "   macOS: brew install python3"
    echo "   Ubuntu: sudo apt-get install python3 python3-pip"
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 no está instalado. Instalando..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y python3-pip
    fi
fi

echo "✅ pip3 encontrado: $(pip3 --version)"

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip3 install -r requirements.txt

# Verificar si UnRAR está instalado
if ! command -v unrar &> /dev/null; then
    echo "⚠️  UnRAR no está instalado. Instalando..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install unrar
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y unrar
    fi
else
    echo "✅ UnRAR encontrado: $(unrar version | head -n1)"
fi

# Verificar si 7zip está instalado (opcional)
if ! command -v 7z &> /dev/null; then
    echo "ℹ️  7zip no está instalado (opcional, pero recomendado como respaldo)"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "   Para instalarlo: brew install p7zip"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "   Para instalarlo: sudo apt-get install p7zip-full"
    fi
else
    echo "✅ 7zip encontrado: $(7z | head -n1)"
fi

echo ""
echo "🎉 ¡Instalación completada!"
echo ""
echo "Para ejecutar el programa:"
echo "  python3 rar_to_zip_converter.py"
echo ""
echo "Para más información, consulta el README.md"
