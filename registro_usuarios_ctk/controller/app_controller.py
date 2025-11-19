import tkinter.messagebox as messagebox
from pathlib import Path
from PIL import Image
import customtkinter as ctk

from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView


class AppController:
    def __init__(self, master):
        self.master = master
        self.modelo = GestorUsuarios()
        self.view = MainView(master)

        # Configurar rutas
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.CSV_PATH = self.BASE_DIR / "usuarios.csv"

        # Caché de imágenes
        self.avatar_images = {}

        # Configurar callbacks
        self.view.configurar_callback_anadir(self.abrir_ventana_anadir)
        self.view.configurar_menu_archivo(
            on_guardar=self.guardar_usuarios,
            on_cargar=self.cargar_usuarios,
            on_salir=self.salir
        )

        # Intentar cargar CSV al inicio
        self.cargar_usuarios()

        # Refrescar la lista
        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuarios = self.modelo.listar()
        usuario = usuarios[indice]
        avatar_image = self.cargar_avatar(usuario.avatar)
        self.view.mostrar_detalles_usuario(usuario, avatar_image)

    def cargar_avatar(self, nombre_archivo):
        if not nombre_archivo:
            return None

        # Si ya está en caché, devolverla
        if nombre_archivo in self.avatar_images:
            return self.avatar_images[nombre_archivo]

        ruta = self.ASSETS_PATH / nombre_archivo
        try:
            imagen = Image.open(ruta)
            ctk_image = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(120, 120))
            self.avatar_images[nombre_archivo] = ctk_image
            return ctk_image
        except FileNotFoundError:
            return None

    def abrir_ventana_anadir(self):
        add_view = AddUserView(self.master)
        add_view.guardar_button.configure(command=lambda: self.anadir_usuario(add_view))

    def anadir_usuario(self, add_view):
        datos = add_view.get_data()
        nombre = datos["nombre"]
        edad_txt = datos["edad"]
        genero = datos["genero"]
        avatar = datos["avatar"]

        # Validaciones
        if not nombre or not edad_txt:
            messagebox.showerror("Error", "Nombre y edad son obligatorios")
            return

        try:
            edad = int(edad_txt)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero")
            return

        # Crear y añadir usuario
        nuevo_usuario = Usuario(nombre, edad, genero, avatar)
        self.modelo.añadir(nuevo_usuario)

        # Cerrar ventana y refrescar
        add_view.window.destroy()
        self.refrescar_lista_usuarios()

    def guardar_usuarios(self):
        try:
            self.modelo.guardar_csv(self.CSV_PATH)
            messagebox.showinfo("Guardar", "Usuarios guardados correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los usuarios.\n{e}")

    def cargar_usuarios(self):
        self.modelo.cargar_csv(self.CSV_PATH)
        self.refrescar_lista_usuarios()
        messagebox.showinfo("Cargar", "Usuarios cargados correctamente")

    def salir(self):
        self.master.destroy()