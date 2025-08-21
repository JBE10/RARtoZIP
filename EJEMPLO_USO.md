# Ejemplo de Uso del Conversor RAR a ZIP

## 🚀 Inicio Rápido

### Opción 1: Usar el script de inicio (Recomendado)
```bash
./run_converter.sh
```

### Opción 2: Ejecutar manualmente
```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar programa
python rar_to_zip_converter.py
```

## 📋 Pasos para Convertir un Archivo

### 1. **Seleccionar Archivo RAR**
- Haz clic en el botón "Examinar" junto a "Archivo RAR:"
- Navega hasta tu archivo .rar
- Selecciónalo y haz clic en "Abrir"

### 2. **Elegir Destino ZIP**
- Haz clic en el botón "Examinar" junto a "Destino ZIP:"
- Elige la carpeta donde quieres guardar el archivo ZIP
- Escribe el nombre del archivo (o déjalo como está)
- Haz clic en "Guardar"

### 3. **Iniciar Conversión**
- Haz clic en el botón "Convertir RAR a ZIP"
- Observa la barra de progreso
- Espera a que termine la conversión

### 4. **¡Listo!**
- Aparecerá un mensaje de éxito
- Tu archivo ZIP estará listo en la ubicación especificada

## 🔧 Características Avanzadas

### Conversión por Lotes
El programa puede convertir múltiples archivos uno por uno:
1. Convierte el primer archivo
2. Cierra el programa
3. Vuelve a abrirlo para el siguiente archivo

### Preservación de Estructura
- ✅ Mantiene carpetas y subcarpetas
- ✅ Preserva nombres de archivos
- ✅ Mantiene la jerarquía original

### Manejo de Errores
- Si un archivo está corrupto, se mostrará un error
- Si no tienes permisos, se te avisará
- Si falta espacio en disco, se detendrá la conversión

## 📁 Ejemplos de Uso

### Ejemplo 1: Archivo Simple
```
Archivo RAR: /Users/usuario/Descargas/documentos.rar
Destino ZIP: /Users/usuario/Desktop/documentos.zip
```

### Ejemplo 2: Con Subcarpetas
```
Archivo RAR: /Users/usuario/Descargas/proyecto_completo.rar
Destino ZIP: /Users/usuario/Desktop/proyecto_completo.zip
```
*Resultado: Mantiene todas las carpetas y archivos del proyecto*

### Ejemplo 3: Archivo Grande
```
Archivo RAR: /Users/usuario/Descargas/video_largo.rar (2GB)
Destino ZIP: /Users/usuario/Desktop/video_largo.zip
```
*El programa mostrará el progreso en tiempo real*

## ⚠️ Solución de Problemas Comunes

### Error: "No se pudo abrir el archivo RAR"
- Verifica que el archivo no esté corrupto
- Asegúrate de que sea un archivo RAR válido
- Intenta con otro archivo RAR

### Error: "Permiso denegado"
- Verifica que tengas permisos de lectura en el archivo RAR
- Verifica que tengas permisos de escritura en la carpeta de destino
- Ejecuta el programa con permisos de administrador si es necesario

### Error: "Espacio insuficiente en disco"
- Libera espacio en el disco de destino
- El archivo ZIP puede ser más grande que el RAR original

### El programa se cuelga
- Cierra el programa y vuelve a abrirlo
- Verifica que no haya otros procesos usando los archivos
- Reinicia tu computadora si es necesario

## 🎯 Consejos de Uso

1. **Nombres de archivo**: Usa nombres simples sin caracteres especiales
2. **Ruta de destino**: Elige una ruta corta y fácil de recordar
3. **Archivos grandes**: Ten paciencia, la conversión puede tomar tiempo
4. **Múltiples archivos**: Convierte uno por uno para mejor control
5. **Verificación**: Siempre verifica que el archivo ZIP se haya creado correctamente

## 🔍 Verificación de Conversión

Después de la conversión, puedes verificar que todo esté correcto:

1. **Abre el archivo ZIP** con tu programa preferido
2. **Compara el contenido** con el archivo RAR original
3. **Verifica el tamaño** del archivo ZIP
4. **Prueba extraer** algunos archivos del ZIP

## 📞 Soporte

Si tienes problemas:
1. Revisa este archivo de ejemplo
2. Consulta el README.md
3. Ejecuta `python test_conversion.py` para verificar la instalación
4. Verifica que tienes UnRAR instalado en tu sistema
