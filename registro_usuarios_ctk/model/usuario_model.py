class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()
    
    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Aang", 112, "Masculino", "aanf.png"))
        self._usuarios.append(Usuario("Roku", 98, "Masculino", "roku.png"))
        self._usuarios.append(Usuario("Kioshi", 257, "Femenino", "kioshi.png"))
    
    def listar(self):
        return self._usuarios
    
    def añadir(self, usuario):
        self._usuarios.append(usuario)