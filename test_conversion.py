#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad del conversor RAR a ZIP
"""

import os
import zipfile
import tempfile
import shutil
from pathlib import Path

from rar_to_zip_converter import convert_rar_to_zip_file

def create_test_rar():
    """Crear un archivo de prueba para simular RAR (en realidad creamos un ZIP temporal)"""
    test_dir = tempfile.mkdtemp()
    
    # Crear algunos archivos de prueba
    test_files = [
        "archivo1.txt",
        "archivo2.txt",
        "carpeta/archivo3.txt",
        "carpeta/subcarpeta/archivo4.txt",
    ]

    for file_path in test_files:
        full_path = os.path.join(test_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"Contenido de {file_path}\n")
            f.write("Este es un archivo de prueba para el conversor RAR a ZIP.\n")

    # Crear un directorio vacío
    empty_dir = os.path.join(test_dir, "carpeta_vacia")
    os.makedirs(empty_dir, exist_ok=True)

    # Crear archivo ZIP temporal (simulando RAR)
    temp_rar = tempfile.NamedTemporaryFile(suffix=".rar", delete=False)
    temp_rar.close()

    with zipfile.ZipFile(temp_rar.name, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(test_dir):
            rel_root = os.path.relpath(root, test_dir)
            if rel_root == ".":
                rel_root = ""
            if not files and not dirs:
                zf.writestr(rel_root + "/", b"")
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.join(rel_root, file)
                zf.write(file_path, arcname)
    
    # Limpiar directorio temporal
    shutil.rmtree(test_dir)
    
    return temp_rar.name

def test_conversion():
    """Probar la conversión RAR a ZIP"""
    print("🧪 Iniciando pruebas del conversor RAR a ZIP...")
    
    # Crear archivo de prueba
    test_rar = create_test_rar()

    # Realizar la conversión
    test_zip = test_rar.replace(".rar", ".zip")
    convert_rar_to_zip_file(test_rar, test_zip)

    # Verificar contenido
    with zipfile.ZipFile(test_rar, "r") as orig, zipfile.ZipFile(test_zip, "r") as conv:
        assert sorted(orig.namelist()) == sorted(conv.namelist())

    # Limpiar archivos temporales
    os.unlink(test_rar)
    os.unlink(test_zip)

if __name__ == "__main__":
    test_conversion()
