#!/bin/bash

# Script para ejecutar el Conversor RAR a ZIP
echo "🚀 Iniciando Conversor RAR a ZIP..."

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Entorno virtual no encontrado. Creando uno nuevo..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    echo "✅ Entorno virtual encontrado. Activando..."
    source venv/bin/activate
fi

# Verificar dependencias
if ! python -c "import rarfile" 2>/dev/null; then
    echo "❌ Dependencias no instaladas. Instalando..."
    pip install -r requirements.txt
fi

echo "✅ Iniciando programa..."
python rar_to_zip_converter.py
