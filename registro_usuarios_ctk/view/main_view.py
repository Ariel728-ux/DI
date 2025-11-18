
"""
Vista principal de la aplicación.
Contiene todos los widgets y la estructura visual.
"""

import customtkinter as ctk


class MainView:
    """Vista principal que muestra la lista de usuarios y sus detalles."""

    def __init__(self, master):
        self.master = master

        # Configurar el grid principal (2 columnas)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=2)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=0)

        # ===== PANEL IZQUIERDO: Lista de Usuarios =====
        self.frame_izquierdo = ctk.CTkFrame(master)
        self.frame_izquierdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Título
        titulo_usuarios = ctk.CTkLabel(
            self.frame_izquierdo,
            text="Usuarios",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo_usuarios.pack(pady=10)

        # Frame scrollable para la lista
        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(
            self.frame_izquierdo,
            width=200
        )
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=10, pady=5)

        # ===== PANEL DERECHO: Detalles del Usuario =====
        self.frame_derecho = ctk.CTkFrame(master)
        self.frame_derecho.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Título
        titulo_detalles = ctk.CTkLabel(
            self.frame_derecho,
            text="Detalles del Usuario",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo_detalles.pack(pady=10)

        # Labels para mostrar información
        self.nombre_label = ctk.CTkLabel(
            self.frame_derecho,
            text="Nombre: -",
            font=ctk.CTkFont(size=14)
        )
        self.nombre_label.pack(pady=5, anchor="w", padx=20)

        self.edad_label = ctk.CTkLabel(
            self.frame_derecho,
            text="Edad: -",
            font=ctk.CTkFont(size=14)
        )
        self.edad_label.pack(pady=5, anchor="w", padx=20)

        self.genero_label = ctk.CTkLabel(
            self.frame_derecho,
            text="Género: -",
            font=ctk.CTkFont(size=14)
        )
        self.genero_label.pack(pady=5, anchor="w", padx=20)

        self.avatar_label_texto = ctk.CTkLabel(
            self.frame_derecho,
            text="Avatar: -",
            font=ctk.CTkFont(size=14)
        )
        self.avatar_label_texto.pack(pady=5, anchor="w", padx=20)

        # Label para la imagen del avatar
        self.avatar_label = ctk.CTkLabel(
            self.frame_derecho,
            text=""
        )
        self.avatar_label.pack(pady=20)

        # ===== PANEL INFERIOR: Botones =====
        self.frame_botones = ctk.CTkFrame(master)
        self.frame_botones.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.btn_agregar = ctk.CTkButton(
            self.frame_botones,
            text="Añadir Usuario",
            width=150
        )
        self.btn_agregar.pack(side="left", padx=10, pady=10)

        self.btn_eliminar = ctk.CTkButton(
            self.frame_botones,
            text="Eliminar Usuario",
            width=150,
            fg_color="red",
            hover_color="darkred"
        )
        self.btn_eliminar.pack(side="left", padx=10, pady=10)

        self.btn_salir = ctk.CTkButton(
            self.frame_botones,
            text="Salir",
            width=150
        )
        self.btn_salir.pack(side="right", padx=10, pady=10)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        """Actualiza la lista de usuarios mostrada."""
        # Limpiar lista actual
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        # Crear botón para cada usuario
        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario):
        """Muestra los detalles de un usuario en el panel derecho."""
        if usuario:
            self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
            self.edad_label.configure(text=f"Edad: {usuario.edad}")
            self.genero_label.configure(text=f"Género: {usuario.genero}")
            self.avatar_label_texto.configure(text=f"Avatar: {usuario.avatar}")
        else:
            self.nombre_label.configure(text="Nombre: -")
            self.edad_label.configure(text="Edad: -")
            self.genero_label.configure(text="Género: -")
            self.avatar_label_texto.configure(text="Avatar: -")