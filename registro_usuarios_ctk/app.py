"""
Punto de entrada de la aplicación.
Configura CustomTkinter y arranca el controlador principal.
"""

import customtkinter as ctk
from controller.app_controller import AppController

if __name__ == "__main__":
    # Configuración de apariencia
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Crear ventana principal
    app = ctk.CTk()
    app.title("Registro de Usuarios (CTk + MVC) - Fase 1")
    app.geometry("800x500")

    # Crear controlador
    controller = AppController(app)

    app.mainloop()