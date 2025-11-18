"""
Controlador principal que orquesta el Modelo y la Vista.
"""

from model.usuario_model import GestorUsuarios
from view.main_view import MainView


class AppController:
    """Controlador principal que coordina Modelo y Vista."""

    def __init__(self, master):
        self.master = master

        # Crear instancias del Modelo y la Vista
        self.modelo = GestorUsuarios()
        self.view = MainView(master)

        # Índice del usuario seleccionado
        self.usuario_seleccionado_idx = None

        # Conectar eventos
        self._conectar_eventos()

        # Refrescar lista inicial
        self.refrescar_lista_usuarios()

    def _conectar_eventos(self):
        """Conecta los widgets de la vista con los métodos del controlador."""
        self.view.btn_salir.configure(command=self.salir)

    def refrescar_lista_usuarios(self):
        """Actualiza la lista de usuarios en la vista."""
        usuarios = self.modelo.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        """Callback cuando se selecciona un usuario de la lista."""
        self.usuario_seleccionado_idx = indice
        usuario = self.modelo.obtener(indice)

        if usuario:
            self.view.mostrar_detalles_usuario(usuario)
        else:
            self.view.mostrar_detalles_usuario(None)

    def salir(self):
        """Cierra la aplicación."""
        self.master.quit()