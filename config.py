# Configuración del Conversor RAR a ZIP
# Modifica estos valores según tus preferencias

# Configuración de la interfaz
UI_CONFIG = {
    'window_title': 'Conversor RAR a ZIP',
    'window_width': 600,
    'window_height': 400,
    'theme': 'clam',  # Opciones: 'clam', 'alt', 'default', 'classic'
    'font_family': 'Helvetica',
    'title_font_size': 16,
    'status_font_size': 10
}

# Configuración de conversión
CONVERSION_CONFIG = {
    'compression_level': 6,  # Nivel de compresión ZIP (1-9, 9 = máxima)
    'preserve_timestamps': True,  # Mantener fechas de modificación
    'create_backup': False,  # Crear copia de seguridad antes de sobrescribir
    'temp_directory': '/tmp',  # Directorio temporal para archivos intermedios
    'max_file_size': 1024 * 1024 * 1024  # Tamaño máximo de archivo (1GB)
}

# Configuración de archivos
FILE_CONFIG = {
    'supported_rar_extensions': ['.rar', '.RAR'],
    'default_zip_extension': '.zip',
    'auto_generate_filename': True,  # Generar nombre automáticamente
    'overwrite_existing': False,  # Preguntar antes de sobrescribir
    'show_hidden_files': False  # Mostrar archivos ocultos en el explorador
}

# Configuración de rendimiento
PERFORMANCE_CONFIG = {
    'use_multithreading': True,  # Usar hilos para conversión
    'chunk_size': 8192,  # Tamaño del chunk para lectura/escritura
    'progress_update_interval': 100,  # Actualizar progreso cada N archivos
    'memory_limit': 512 * 1024 * 1024  # Límite de memoria (512MB)
}

# Configuración de logging
LOGGING_CONFIG = {
    'enable_logging': True,
    'log_level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    'log_file': 'converter.log',
    'max_log_size': 1024 * 1024,  # 1MB
    'backup_count': 3
}

# Configuración de idioma
LANGUAGE_CONFIG = {
    'language': 'es',  # 'es' para español, 'en' para inglés
    'texts': {
        'es': {
            'title': 'Conversor RAR a ZIP',
            'select_rar': 'Archivo RAR:',
            'select_zip': 'Destino ZIP:',
            'browse': 'Examinar',
            'convert': 'Convertir RAR a ZIP',
            'progress': 'Progreso:',
            'status_ready': 'Listo para convertir',
            'status_converting': 'Convirtiendo...',
            'status_complete': 'Conversión completada exitosamente!',
            'error_no_rar': 'Por favor selecciona un archivo RAR',
            'error_no_destination': 'Por favor selecciona un destino para el archivo ZIP',
            'success_message': 'El archivo RAR ha sido convertido a ZIP correctamente'
        },
        'en': {
            'title': 'RAR to ZIP Converter',
            'select_rar': 'RAR File:',
            'select_zip': 'ZIP Destination:',
            'browse': 'Browse',
            'convert': 'Convert RAR to ZIP',
            'progress': 'Progress:',
            'status_ready': 'Ready to convert',
            'status_converting': 'Converting...',
            'status_complete': 'Conversion completed successfully!',
            'error_no_rar': 'Please select a RAR file',
            'error_no_destination': 'Please select a destination for the ZIP file',
            'success_message': 'The RAR file has been converted to ZIP successfully'
        }
    }
}
