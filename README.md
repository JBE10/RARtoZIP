# Conversor RAR a ZIP

Un programa en Python con interfaz gráfica para convertir archivos RAR a ZIP de forma perfecta.

## Características

- 🖥️ **Interfaz gráfica moderna** usando tkinter
- 📁 **Selección fácil** de archivos RAR y destino ZIP
- 🔄 **Conversión perfecta** preservando estructura de archivos
- 📊 **Barra de progreso** en tiempo real
- 🚀 **Conversión rápida** usando hilos separados
- 🛡️ **Manejo de errores** robusto
- 🔧 **Método alternativo** usando 7zip como respaldo

## Instalación

### 1. Instalar Python
Asegúrate de tener Python 3.7 o superior instalado en tu sistema.

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Instalar UnRAR (requerido para rarfile)
- **macOS**: `brew install unrar`
- **Ubuntu/Debian**: `sudo apt-get install unrar`
- **Windows**: Descarga desde [WinRAR](https://www.win-rar.com/)

## Uso

### Ejecutar el programa
```bash
python rar_to_zip_converter.py
```

### Pasos para convertir:
1. **Seleccionar archivo RAR**: Haz clic en "Examinar" y elige tu archivo .rar
2. **Elegir destino ZIP**: Haz clic en "Examinar" para el destino (se auto-genera si no lo especificas)
3. **Convertir**: Haz clic en "Convertir RAR a ZIP"
4. **Esperar**: El programa mostrará el progreso en tiempo real
5. **¡Listo!**: Tu archivo ZIP estará listo en la ubicación especificada

## Funcionamiento

El programa utiliza la librería `rarfile` para leer archivos RAR y `zipfile` para crear archivos ZIP. El proceso:

1. Abre el archivo RAR
2. Lee cada archivo contenido
3. Lo escribe en el nuevo archivo ZIP
4. Preserva la estructura de directorios original
5. Mantiene la integridad de los datos

## Solución de problemas

### Error: "rarfile no está instalado"
```bash
pip install rarfile
```

### Error: "No se pudo abrir el archivo RAR"
- Verifica que el archivo RAR no esté corrupto
- Asegúrate de tener UnRAR instalado
- El programa intentará usar 7zip como alternativa

### Error: "Permiso denegado"
- Ejecuta el programa con permisos de administrador
- Verifica que tengas permisos de escritura en la carpeta de destino

## Requisitos del sistema

- Python 3.7+
- UnRAR o 7zip instalado
- Suficiente espacio en disco para el archivo ZIP resultante
- Permisos de lectura/escritura en las carpetas de origen y destino

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.
