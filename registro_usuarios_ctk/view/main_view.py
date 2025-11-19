import customtkinter as ctk
import tkinter


class MainView:
    def __init__(self, master):
        self.master = master

        # Crear menú
        self.menubar = tkinter.Menu(master)
        master.config(menu=self.menubar)
        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        # Configurar grid principal
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)

        # Frame izquierdo - Lista de usuarios
        self.frame_izquierdo = ctk.CTkFrame(self.master)
        self.frame_izquierdo.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)

        self.label_titulo_lista = ctk.CTkLabel(
            self.frame_izquierdo,
            text="Lista de Usuarios",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.label_titulo_lista.pack(pady=10)

        # Botón para añadir usuario
        self.boton_anadir = ctk.CTkButton(
            self.frame_izquierdo,
            text="Añadir Usuario"
        )
        self.boton_anadir.pack(pady=5, padx=10, fill="x")

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.frame_izquierdo)
        self.lista_usuarios_scrollable.pack(expand=True, fill="both", padx=10, pady=10)

        # Frame derecho - Detalles del usuario
        self.frame_derecho = ctk.CTkFrame(self.master)
        self.frame_derecho.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=10)

        self.label_titulo_detalles = ctk.CTkLabel(
            self.frame_derecho,
            text="Detalles del Usuario",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.label_titulo_detalles.pack(pady=10)

        # Label para el avatar
        self.avatar_label = ctk.CTkLabel(self.frame_derecho, text="")
        self.avatar_label.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.frame_derecho, text="Nombre: -")
        self.label_nombre.pack(pady=5, padx=20, anchor="w")

        self.label_edad = ctk.CTkLabel(self.frame_derecho, text="Edad: -")
        self.label_edad.pack(pady=5, padx=20, anchor="w")

        self.label_genero = ctk.CTkLabel(self.frame_derecho, text="Género: -")
        self.label_genero.pack(pady=5, padx=20, anchor="w")

    def configurar_menu_archivo(self, on_guardar, on_cargar, on_salir):
        self.menu_archivo.add_command(label="Guardar", command=on_guardar)
        self.menu_archivo.add_command(label="Cargar", command=on_cargar)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=on_salir)

    def configurar_callback_anadir(self, callback):
        self.boton_anadir.configure(command=callback)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        # Limpiar lista anterior
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        # Crear botones para cada usuario
        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario, avatar_image=None):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")

        if avatar_image:
            self.avatar_label.configure(image=avatar_image, text="")
        else:
            self.avatar_label.configure(image="", text="Sin avatar")


class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x400")
        self.window.grab_set()

        # Nombre
        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=(20, 5), padx=20, anchor="w")
        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.pack(pady=5, padx=20, fill="x")

        # Edad
        ctk.CTkLabel(self.window, text="Edad:").pack(pady=(10, 5), padx=20, anchor="w")
        self.edad_entry = ctk.CTkEntry(self.window)
        self.edad_entry.pack(pady=5, padx=20, fill="x")

        # Género
        ctk.CTkLabel(self.window, text="Género:").pack(pady=(10, 5), padx=20, anchor="w")
        self.genero_var = ctk.StringVar(value="Masculino")
        ctk.CTkRadioButton(
            self.window,
            text="Masculino",
            variable=self.genero_var,
            value="Masculino"
        ).pack(padx=30, anchor="w")
        ctk.CTkRadioButton(
            self.window,
            text="Femenino",
            variable=self.genero_var,
            value="Femenino"
        ).pack(padx=30, anchor="w")
        ctk.CTkRadioButton(
            self.window,
            text="Otro",
            variable=self.genero_var,
            value="Otro"
        ).pack(padx=30, anchor="w")

        # Avatar
        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=(10, 5), padx=20, anchor="w")
        self.avatar_var = ctk.StringVar(value="mujer 1.png")
        ctk.CTkRadioButton(
            self.window,
            text="Mujer 1",
            variable=self.avatar_var,
            value="mujer 1.png"
        ).pack(padx=30, anchor="w")
        ctk.CTkRadioButton(
            self.window,
            text="Hombre",
            variable=self.avatar_var,
            value="hombre.png"
        ).pack(padx=30, anchor="w")
        ctk.CTkRadioButton(
            self.window,
            text="Mujer 2",
            variable=self.avatar_var,
            value="mujer 2.png"
        ).pack(padx=30, anchor="w")

        # Botones
        self.guardar_button = ctk.CTkButton(self.window, text="Guardar")
        self.guardar_button.pack(pady=20, padx=20, fill="x")

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get().strip(),
            "edad": self.edad_entry.get().strip(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_var.get()
        }