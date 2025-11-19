import threading
import tkinter.messagebox as messagebox
from pathlib import Path
from PIL import Image
import customtkinter as ctk

from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView, EditUserView


class AppController:
    def __init__(self, master):
        self.master = master
        self.modelo = GestorUsuarios()
        self.view = MainView(master)

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.CSV_PATH = self.BASE_DIR / "usuarios.csv"

        self.avatar_images = {}
        self.indices_visibles = []
        self.usuario_actual = None

        # Control de auto-guardado
        self.auto_guardar_activo = False
        self._auto_guardar_stop = threading.Event()
        self._auto_guardar_thread = None

        self.view.configurar_callback_anadir(self.abrir_ventana_anadir)
        self.view.configurar_callback_eliminar(self.eliminar_usuario)
        self.view.configurar_menu_archivo(
            on_guardar=self.guardar_usuarios,
            on_cargar=self.cargar_usuarios,
            on_salir=self.salir
        )
        self.view.configurar_callbacks_filtro(self.aplicar_filtros_y_actualizar)
        self.view.configurar_callback_autoguardar(self.toggle_auto_guardado)
        self.view.configurar_callback_salir(self.salir)

        self.modelo.cargar_csv(self.CSV_PATH)
        self.aplicar_filtros_y_actualizar()

    def aplicar_filtros_y_actualizar(self):
        texto_busqueda = self.view.get_texto_busqueda().strip().lower()
        filtro_genero = self.view.get_filtro_genero()

        todos_usuarios = self.modelo.listar()
        self.indices_visibles = []

        for i, usuario in enumerate(todos_usuarios):
            cumple_busqueda = texto_busqueda == "" or texto_busqueda in usuario.nombre.lower()
            cumple_genero = filtro_genero == "Todos" or usuario.genero == filtro_genero

            if cumple_busqueda and cumple_genero:
                self.indices_visibles.append(i)

        usuarios_filtrados = [todos_usuarios[i] for i in self.indices_visibles]
        self.view.actualizar_lista_usuarios(
            usuarios_filtrados,
            self.seleccionar_usuario,
            self.abrir_ventana_editar
        )

        total = len(todos_usuarios)
        visibles = len(usuarios_filtrados)
        self.view.actualizar_estado(f"Usuarios visibles: {visibles}/{total}")

        if visibles > 0:
            self.seleccionar_usuario(0)

    def seleccionar_usuario(self, indice_vista):
        if indice_vista >= len(self.indices_visibles):
            return

        indice_real = self.indices_visibles[indice_vista]
        self.usuario_actual = indice_real
        usuario = self.modelo.obtener(indice_real)
        avatar_image = self.cargar_avatar(usuario.avatar)
        self.view.mostrar_detalles_usuario(usuario, avatar_image)

    def cargar_avatar(self, nombre_archivo):
        if not nombre_archivo:
            return None

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

        if not nombre or not edad_txt:
            messagebox.showerror("Error", "Nombre y edad son obligatorios")
            return

        try:
            edad = int(edad_txt)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero")
            return
        nuevo_usuario = Usuario(nombre, edad, genero, avatar)
        self.modelo.añadir(nuevo_usuario)

        add_view.window.destroy()
        self.aplicar_filtros_y_actualizar()
        self.view.actualizar_estado("Usuario añadido correctamente")

    def abrir_ventana_editar(self, indice_vista):
        if indice_vista >= len(self.indices_visibles):
            return

        indice_real = self.indices_visibles[indice_vista]
        usuario = self.modelo.obtener(indice_real)

        edit_view = EditUserView(self.master, usuario)
        edit_view.guardar_button.configure(
            command=lambda: self.guardar_edicion_usuario(edit_view, indice_real)
        )

    def guardar_edicion_usuario(self, edit_view, indice):
        datos = edit_view.get_data()
        nombre = datos["nombre"]
        edad_txt = datos["edad"]
        genero = datos["genero"]
        avatar = datos["avatar"]

        if not nombre or not edad_txt:
            messagebox.showerror("Error", "Nombre y edad son obligatorios")
            return

        try:
            edad = int(edad_txt)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero")
            return

        usuario = self.modelo.obtener(indice)
        usuario.nombre = nombre
        usuario.edad = edad
        usuario.genero = genero
        usuario.avatar = avatar

        edit_view.window.destroy()
        self.aplicar_filtros_y_actualizar()
        self.view.actualizar_estado("Usuario editado correctamente")

    def eliminar_usuario(self):
        if self.usuario_actual is None:
            messagebox.showwarning("Advertencia", "No hay usuario seleccionado")
            return

        if not messagebox.askyesno("Confirmar", "¿Eliminar el usuario seleccionado?"):
            return

        self.modelo.eliminar(self.usuario_actual)
        self.usuario_actual = None
        self.aplicar_filtros_y_actualizar()
        self.view.actualizar_estado("Usuario eliminado correctamente")

    def guardar_usuarios(self):
        try:
            self.modelo.guardar_csv(self.CSV_PATH)
            self.view.actualizar_estado("Usuarios guardados correctamente")
            messagebox.showinfo("Guardar", "Usuarios guardados correctamente")
        except Exception as e:
            self.view.actualizar_estado("Error al guardar usuarios")
            messagebox.showerror("Error", f"No se pudieron guardar los usuarios.\n{e}")

    def cargar_usuarios(self):
        self.modelo.cargar_csv(self.CSV_PATH)
        self.aplicar_filtros_y_actualizar()
        self.view.actualizar_estado("Usuarios cargados correctamente")
        messagebox.showinfo("Cargar", "Usuarios cargados correctamente")

    def toggle_auto_guardado(self):
        if not self.auto_guardar_activo:
            # Activar auto-guardado
            self.auto_guardar_activo = True
            self._auto_guardar_stop.clear()
            self._auto_guardar_thread = threading.Thread(
                target=self._auto_guardar_loop,
                daemon=True
            )
            self._auto_guardar_thread.start()
            self.view.set_estado_autoguardar(True)
            self.view.actualizar_estado("Auto-guardado activado (cada 10 segundos)")
        else:
            # Desactivar auto-guardado
            self.auto_guardar_activo = False
            self._auto_guardar_stop.set()
            self.view.set_estado_autoguardar(False)
            self.view.actualizar_estado("Auto-guardado desactivado")

    def _auto_guardar_loop(self):
        while not self._auto_guardar_stop.wait(10.0):
            try:
                self.modelo.guardar_csv(self.CSV_PATH)
                self.master.after(
                    0,
                    lambda: self.view.actualizar_estado("Auto-guardado realizado correctamente")
                )
            except Exception as e:
                self.master.after(
                    0,
                    lambda: self.view.actualizar_estado(f"Error en auto-guardado: {e}")
                )

    def salir(self):
        if self.auto_guardar_activo:
            self.auto_guardar_activo = False
            self._auto_guardar_stop.set()
            if self._auto_guardar_thread and self._auto_guardar_thread.is_alive():
                self._auto_guardar_thread.join(timeout=1)

        self.master.destroy()