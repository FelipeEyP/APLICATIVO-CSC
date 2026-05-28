import customtkinter as ctk
import requests
import json
import os
import sys
import threading
import subprocess
import tempfile
import urllib.request

# --- CONFIGURACIÓN DE LA APP ---
APP_VERSION = "2.0.1" # Cambiado para forzar al robot a trabajar
# Esta URL apunta al raw de tu archivo version.json en tu GitHub
UPDATE_URL = "https://raw.githubusercontent.com/FelipeEyP/APLICATIVO-CSC/refs/heads/main/version.json" 

class ModernApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Aplicativo CSC - v{APP_VERSION}")
        self.geometry("600x400")
        
        # Configuración de apariencia
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # --- CARGAR ÍCONO ---
        try:
            # PyInstaller extrae los archivos a una carpeta temporal (sys._MEIPASS)
            if hasattr(sys, '_MEIPASS'):
                icon_path = os.path.join(sys._MEIPASS, "app_icon.ico")
            else:
                icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_icon.ico")
            self.iconbitmap(icon_path)
        except Exception as e:
            print("No se pudo cargar el icono:", e)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -----------------------------------------------------
        # 1. PANTALLA DE BLOQUEO / CARGA (Visible al iniciar)
        # -----------------------------------------------------
        self.overlay_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.overlay_frame.grid(row=0, column=0, sticky="nsew")
        self.overlay_frame.grid_columnconfigure(0, weight=1)
        
        self.status_label = ctk.CTkLabel(self.overlay_frame, text="Verificando conexión a internet...", font=ctk.CTkFont(size=18, weight="bold"), text_color="orange")
        self.status_label.grid(row=0, column=0, pady=(130, 20))
        
        self.action_btn = ctk.CTkButton(self.overlay_frame, text="Reintentar", command=self.start_update_check)
        self.action_btn.grid(row=1, column=0, pady=10)
        self.action_btn.grid_remove() # Oculto al inicio

        # -----------------------------------------------------
        # 2. PANTALLA PRINCIPAL DE TU APP (Oculta al inicio)
        # -----------------------------------------------------
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Aquí es donde pondrás todos los botones y lógica de tu aplicativo
        self.title_label = ctk.CTkLabel(self.main_frame, text="¡Bienvenido al Aplicativo CSC!", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, pady=(60, 20))
        
        self.content_label = ctk.CTkLabel(self.main_frame, text="Si ves esta pantalla, significa que tienes internet\ny estás usando la versión más reciente del sistema.", text_color="gray")
        self.content_label.grid(row=1, column=0, pady=10)
        
        self.test_btn = ctk.CTkButton(self.main_frame, text="Botón de Prueba (Tu app va aquí)", fg_color="green", hover_color="darkgreen")
        self.test_btn.grid(row=2, column=0, pady=30)

        # -----------------------------------------------------
        # Iniciar la validación automáticamente al abrir
        # -----------------------------------------------------
        self.start_update_check()
        
    def start_update_check(self):
        self.action_btn.grid_remove()
        self.status_label.configure(text="Verificando conexión y seguridad...", text_color="orange")
        threading.Thread(target=self.check_for_updates, daemon=True).start()

    def check_for_updates(self):
        try:
            # Intentar conectar a internet (a tu GitHub)
            response = requests.get(UPDATE_URL, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            remote_version = data.get("version")
            download_url = data.get("download_url")

            # Si hay internet, verificar versión
            if self.is_newer_version(remote_version, APP_VERSION):
                self.status_label.configure(text=f"Actualización obligatoria (v{remote_version})\nDebes actualizar para continuar.", text_color="#00FF00")
                self.action_btn.configure(text="Actualizar Ahora", state="normal", command=lambda: self.start_download(download_url))
                self.action_btn.grid() # Mostrar botón de actualizar
            else:
                # Todo bien: hay internet y es la versión correcta. ¡DESBLOQUEAR APP!
                self.unlock_app()

        except Exception as e:
            # Falló el internet o no pudo conectarse
            self.status_label.configure(text="ERROR CRÍTICO: No hay conexión a internet.\nEl sistema requiere conexión para funcionar.", text_color="red")
            self.action_btn.configure(text="Reintentar conexión", state="normal", command=self.start_update_check)
            self.action_btn.grid()

    def unlock_app(self):
        """Oculta la pantalla de bloqueo y muestra tu aplicación real"""
        self.overlay_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky="nsew")

    def is_newer_version(self, remote, local):
        try:
            remote_parts = [int(x) for x in remote.split(".")]
            local_parts = [int(x) for x in local.split(".")]
            return remote_parts > local_parts
        except:
            return False

    def start_download(self, download_url):
        self.action_btn.configure(state="disabled", text="Descargando...")
        threading.Thread(target=self.download_and_install, args=(download_url,), daemon=True).start()

    def download_and_install(self, download_url):
        try:
            self.status_label.configure(text="Descargando nueva versión...\nPor favor, no cierres esta ventana.", text_color="orange")
            
            temp_dir = tempfile.gettempdir()
            installer_path = os.path.join(temp_dir, "app_update.exe")
            
            urllib.request.urlretrieve(download_url, installer_path)
            
            self.status_label.configure(text="¡Descarga completa! Instalando...", text_color="#00FF00")
            
            subprocess.Popen([installer_path])
            os._exit(0)

        except Exception as e:
            self.status_label.configure(text="Error al descargar la actualización.\nRevisa tu internet.", text_color="red")
            self.action_btn.configure(text="Reintentar descarga", state="normal", command=lambda: self.start_download(download_url))
            print(f"Error download: {e}")

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
