@echo off
echo 🚀 Instalando Conversor RAR a ZIP...
echo ======================================

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado. Por favor instálalo desde https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado
python --version

REM Verificar si pip está instalado
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip no está instalado. Instalando...
    python -m ensurepip --upgrade
)

echo ✅ pip encontrado
pip --version

REM Instalar dependencias de Python
echo 📦 Instalando dependencias de Python...
pip install -r requirements.txt

REM Verificar si WinRAR está instalado
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WinRAR" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  WinRAR no está instalado. Por favor instálalo desde https://www.win-rar.com/
    echo    El programa funcionará pero es recomendado para mejor compatibilidad.
) else (
    echo ✅ WinRAR encontrado
)

REM Verificar si 7zip está instalado
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\7-Zip" >nul 2>&1
if errorlevel 1 (
    echo ℹ️  7zip no está instalado (opcional, pero recomendado como respaldo)
    echo    Para instalarlo: https://7-zip.org/
) else (
    echo ✅ 7zip encontrado
)

echo.
echo 🎉 ¡Instalación completada!
echo.
echo Para ejecutar el programa:
echo   python rar_to_zip_converter.py
echo.
echo Para más información, consulta el README.md
pause
