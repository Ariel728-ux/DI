"""
Modelo de datos para el sistema de registro de usuarios.
Contiene la lógica de negocio y gestión de datos.
"""


class Usuario:
    """Representa un usuario con sus datos básicos."""

    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __str__(self):
        return f"Usuario({self.nombre}, {self.edad} años, {self.genero})"


class GestorUsuarios:
    """Gestiona la colección de usuarios y operaciones sobre ellos."""

    def __init__(self):
        # Lista interna de usuarios
        self._usuarios = []
        # Cargar datos de ejemplo al inicio
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        """Carga algunos usuarios de prueba para desarrollo."""
        usuarios_ejemplo = [
            Usuario("Ana García", 28, "Femenino", "avatar1.png"),
            Usuario("Luis Pérez", 35, "Masculino", "avatar2.png"),
            Usuario("Sofía Romero", 22, "Femenino", "avatar3.png")
        ]
        self._usuarios.extend(usuarios_ejemplo)

    def listar(self):
        """Devuelve la lista completa de usuarios."""
        return self._usuarios

    def obtener(self, indice):
        """Obtiene un usuario por su índice."""
        if 0 <= indice < len(self._usuarios):
            return self._usuarios[indice]
        return None

    def agregar(self, usuario):
        """Añade un nuevo usuario a la lista."""
        if isinstance(usuario, Usuario):
            self._usuarios.append(usuario)
            return True
        return False

    def eliminar(self, indice):
        """Elimina un usuario por su índice."""
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
            return True
        return False