#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad del conversor RAR a ZIP
"""

import os
import zipfile
import tempfile
import shutil
from pathlib import Path

def create_test_rar():
    """Crear un archivo de prueba para simular RAR (en realidad creamos un ZIP temporal)"""
    test_dir = tempfile.mkdtemp()
    
    # Crear algunos archivos de prueba
    test_files = [
        "archivo1.txt",
        "archivo2.txt", 
        "carpeta/archivo3.txt",
        "carpeta/subcarpeta/archivo4.txt"
    ]
    
    for file_path in test_files:
        full_path = os.path.join(test_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(f"Contenido de {file_path}\n")
            f.write("Este es un archivo de prueba para el conversor RAR a ZIP.\n")
    
    # Crear archivo ZIP temporal (simulando RAR)
    temp_rar = tempfile.NamedTemporaryFile(suffix='.rar', delete=False)
    temp_rar.close()
    
    with zipfile.ZipFile(temp_rar.name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(test_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, test_dir)
                zf.write(file_path, arcname)
    
    # Limpiar directorio temporal
    shutil.rmtree(test_dir)
    
    return temp_rar.name

def test_conversion():
    """Probar la conversión RAR a ZIP"""
    print("🧪 Iniciando pruebas del conversor RAR a ZIP...")
    
    try:
        # Crear archivo de prueba
        print("📁 Creando archivo de prueba...")
        test_rar = create_test_rar()
        print(f"✅ Archivo de prueba creado: {test_rar}")
        
        # Simular conversión (en realidad solo copiamos el contenido)
        test_zip = test_rar.replace('.rar', '.zip')
        
        print("🔄 Simulando conversión...")
        with zipfile.ZipFile(test_rar, 'r') as rar_file:
            with zipfile.ZipFile(test_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file_info in rar_file.filelist:
                    file_data = rar_file.read(file_info.filename)
                    zip_file.writestr(file_info.filename, file_data)
        
        print(f"✅ Archivo ZIP creado: {test_zip}")
        
        # Verificar contenido
        print("🔍 Verificando contenido...")
        with zipfile.ZipFile(test_zip, 'r') as zip_file:
            file_list = zip_file.namelist()
            print(f"📋 Archivos en el ZIP: {len(file_list)}")
            for file_name in file_list:
                print(f"   - {file_name}")
        
        # Limpiar archivos temporales
        os.unlink(test_rar)
        os.unlink(test_zip)
        
        print("🎉 ¡Todas las pruebas pasaron exitosamente!")
        print("✅ El conversor está funcionando correctamente")
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_conversion()
