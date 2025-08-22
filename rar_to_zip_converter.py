import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import zipfile
import rarfile
import os
import threading
from pathlib import Path
import shutil


def _is_dir(info):
    """Return True if the archive entry represents a directory."""
    if hasattr(info, "is_dir"):
        return info.is_dir()
    if hasattr(info, "isdir"):
        return info.isdir()
    return False


def convert_rar_to_zip_file(rar_path, zip_path, progress_callback=None):
    """Convert a RAR (or ZIP) archive to a ZIP file preserving directories."""

    opener = rarfile.RarFile if rarfile.is_rarfile(rar_path) else zipfile.ZipFile

    with opener(rar_path, "r") as archive, zipfile.ZipFile(
        zip_path, "w", zipfile.ZIP_DEFLATED
    ) as zip_file:
        info_list = archive.infolist()
        files = [info for info in info_list if not _is_dir(info)]
        total = len(files) or 1
        processed = 0

        for info in info_list:
            name = info.filename
            if _is_dir(info):
                # Asegurarnos de que las entradas de directorio terminen con '/'
                if not name.endswith("/"):
                    name += "/"
                zip_file.writestr(name, b"")
                continue

            with archive.open(info) as source:
                zip_file.writestr(name, source.read())

            processed += 1
            if progress_callback:
                progress_callback(processed, total, name)

class RARtoZIPConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor RAR a ZIP")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables
        self.rar_file_path = tk.StringVar()
        self.zip_destination_path = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="Conversor RAR a ZIP", 
                               font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Selección de archivo RAR
        ttk.Label(main_frame, text="Archivo RAR:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.rar_file_path, width=50, state="readonly").grid(row=1, column=1, padx=(10, 5), pady=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_rar_file).grid(row=1, column=2, pady=5)
        
        # Selección de destino ZIP
        ttk.Label(main_frame, text="Destino ZIP:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.zip_destination_path, width=50, state="readonly").grid(row=2, column=1, padx=(10, 5), pady=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_zip_destination).grid(row=2, column=2, pady=5)
        
        # Barra de progreso
        ttk.Label(main_frame, text="Progreso:").grid(row=3, column=0, sticky=tk.W, pady=(20, 5))
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, 
                                          maximum=100, length=400)
        self.progress_bar.grid(row=3, column=1, columnspan=2, pady=(20, 5), sticky=(tk.W, tk.E))
        
        # Botón de conversión
        self.convert_button = ttk.Button(main_frame, text="Convertir RAR a ZIP", 
                                       command=self.start_conversion, style="Accent.TButton")
        self.convert_button.grid(row=4, column=0, columnspan=3, pady=20)
        
        # Estado
        self.status_label = ttk.Label(main_frame, text="Listo para convertir", 
                                     font=("Helvetica", 10))
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # Configurar grid
        main_frame.columnconfigure(1, weight=1)
        
    def browse_rar_file(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo RAR",
            filetypes=[("Archivos RAR", "*.rar"), ("Todos los archivos", "*.*")]
        )
        if filename:
            self.rar_file_path.set(filename)
            # Auto-generar nombre de destino ZIP
            if not self.zip_destination_path.get():
                zip_path = str(Path(filename).with_suffix('.zip'))
                self.zip_destination_path.set(zip_path)
    
    def browse_zip_destination(self):
        filename = filedialog.asksaveasfilename(
            title="Guardar archivo ZIP como",
            defaultextension=".zip",
            filetypes=[("Archivos ZIP", "*.zip"), ("Todos los archivos", "*.*")]
        )
        if filename:
            self.zip_destination_path.set(filename)
    
    def start_conversion(self):
        if not self.rar_file_path.get():
            messagebox.showerror("Error", "Por favor selecciona un archivo RAR")
            return
        
        if not self.zip_destination_path.get():
            messagebox.showerror("Error", "Por favor selecciona un destino para el archivo ZIP")
            return
        
        # Deshabilitar botones durante la conversión
        self.convert_button.config(state="disabled")
        self.progress_var.set(0)
        
        # Iniciar conversión en hilo separado
        conversion_thread = threading.Thread(target=self.convert_rar_to_zip)
        conversion_thread.daemon = True
        conversion_thread.start()
    
    def convert_rar_to_zip(self):
        try:
            rar_path = self.rar_file_path.get()
            zip_path = self.zip_destination_path.get()

            self.update_status("Iniciando conversión...")
            self.progress_var.set(10)

            # Verificar que el archivo RAR existe
            if not os.path.exists(rar_path):
                raise FileNotFoundError(f"No se encontró el archivo: {rar_path}")

            def progress_cb(processed, total, name):
                progress = 10 + processed / total * 80
                self.progress_var.set(progress)
                self.update_status(f"Convirtiendo: {name}")

            try:
                self.update_status("Intentando conversión con rarfile...")
                convert_rar_to_zip_file(rar_path, zip_path, progress_cb)
                self.update_status("Conversión con rarfile completada")
            except Exception as rar_error:
                self.update_status(f"rarfile falló: {str(rar_error)}")
                # Fallback: usar 7zip si está disponible
                try:
                    self.update_status("Intentando método alternativo con 7zip...")
                    self.convert_with_7zip(rar_path, zip_path)
                except Exception as zip_error:
                    self.update_status(f"7zip falló: {str(zip_error)}")
                    # Último recurso: intentar con unar
                    self.update_status("Intentando con unar como último recurso...")
                    self.convert_with_unar(rar_path, zip_path)

            self.progress_var.set(100)
            self.update_status("Conversión completada exitosamente!")
            messagebox.showinfo("Éxito", "El archivo RAR ha sido convertido a ZIP correctamente")

        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error durante la conversión:\n{str(e)}")

        finally:
            # Rehabilitar botones
            self.root.after(0, lambda: self.convert_button.config(state="normal"))
    
    def convert_with_7zip(self, rar_path, zip_path):
        """Método alternativo usando 7zip si está disponible"""
        try:
            import subprocess
            import tempfile
            
            self.update_status("Intentando conversión directa RAR a ZIP con 7zip...")
            
            # Método 1: Intentar conversión directa usando 7zip
            try:
                result = subprocess.run([
                    '7z', 'a', zip_path, rar_path, '-tzip'
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.update_status("Conversión directa exitosa con 7zip")
                    return
                else:
                    self.update_status(f"Conversión directa falló: {result.stderr}")
            except Exception as direct_error:
                self.update_status(f"Conversión directa no disponible: {str(direct_error)}")
            
            # Método 2: Extraer y reempaquetar (fallback)
            self.update_status("Usando método de extracción y reempaquetado...")
            
            with tempfile.TemporaryDirectory() as temp_dir:
                self.update_status(f"Extrayendo a directorio temporal: {temp_dir}")
                
                # Intentar usar 7zip para extraer con formato específico
                result = subprocess.run([
                    '7z', 'x', rar_path, f'-o{temp_dir}', '-y', '-r'
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    # Si falla, intentar con diferentes opciones
                    self.update_status("Primer intento falló, probando método alternativo...")
                    result = subprocess.run([
                        '7z', 'e', rar_path, f'-o{temp_dir}', '-y', '-r'
                    ], capture_output=True, text=True)
                    
                    if result.returncode != 0:
                        error_msg = f"7zip falló con código {result.returncode}: {result.stderr}"
                        self.update_status(error_msg)
                        raise Exception(error_msg)
                
                self.update_status("Creando archivo ZIP...")
                
                # Crear ZIP desde archivos extraídos
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for root, dirs, files in os.walk(temp_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, temp_dir)
                            zip_file.write(file_path, arcname)
                            self.update_status(f"Agregando: {arcname}")
                
                self.update_status("Limpieza completada")
                
        except Exception as e:
            raise Exception(f"Error con 7zip: {str(e)}")
    
    def convert_with_unar(self, rar_path, zip_path):
        """Método alternativo usando unar si está disponible"""
        try:
            import subprocess
            import tempfile
            
            self.update_status("Intentando con unar...")
            
            with tempfile.TemporaryDirectory() as temp_dir:
                self.update_status(f"Extrayendo con unar a: {temp_dir}")
                
                # Intentar extraer con unar
                result = subprocess.run([
                    'unar', '-o', temp_dir, rar_path
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    raise Exception(f"unar falló: {result.stderr}")
                
                self.update_status("Creando ZIP desde archivos extraídos...")
                
                # Crear ZIP desde archivos extraídos
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for root, dirs, files in os.walk(temp_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, temp_dir)
                            zip_file.write(file_path, arcname)
                            self.update_status(f"Agregando: {arcname}")
                
                self.update_status("unar conversión completada")
                
        except Exception as e:
            raise Exception(f"Error con unar: {str(e)}")
    
    def update_status(self, message):
        self.root.after(0, lambda: self.status_label.config(text=message))

def check_dependencies():
    """Verificar que las dependencias necesarias estén disponibles"""
    missing_deps = []
    
    try:
        import rarfile
        print("✓ rarfile disponible")
    except ImportError:
        missing_deps.append("rarfile")
        print("✗ rarfile no disponible")
    
    # Verificar 7zip
    try:
        import subprocess
        result = subprocess.run(['7z'], capture_output=True, text=True)
        if result.returncode == 0 or result.returncode == 7:  # 7zip devuelve 7 para ayuda
            print("✓ 7zip disponible")
        else:
            missing_deps.append("7zip")
            print("✗ 7zip no disponible")
    except Exception:
        missing_deps.append("7zip")
        print("✗ 7zip no disponible")
    
    # Verificar unar
    try:
        import subprocess
        result = subprocess.run(['unar'], capture_output=True, text=True)
        if result.returncode == 0 or result.returncode == 1:  # unar devuelve 1 para ayuda
            print("✓ unar disponible")
        else:
            missing_deps.append("unar")
            print("✗ unar no disponible")
    except Exception:
        missing_deps.append("unar")
        print("✗ unar no disponible")
    
    return missing_deps

def main():
    # Verificar dependencias
    missing_deps = check_dependencies()
    
    if len(missing_deps) == 2:
        messagebox.showerror("Error", 
                           "No se encontraron las dependencias necesarias.\n"
                           "Instala al menos una de estas opciones:\n"
                           "- pip install rarfile\n"
                           "- brew install p7zip")
        return
    elif len(missing_deps) == 1:
        print(f"⚠ Advertencia: {missing_deps[0]} no disponible, pero el programa puede funcionar")
    
    root = tk.Tk()
    app = RARtoZIPConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
