import csv
from pathlib import Path


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

    def guardar_csv(self, ruta):
        ruta = Path(ruta)
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "edad", "genero", "avatar"])
            for u in self._usuarios:
                writer.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta):
        ruta = Path(ruta)
        try:
            with open(ruta, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # Saltar cabecera

                self._usuarios.clear()

                for row in reader:
                    try:
                        if len(row) != 4:
                            continue
                        nombre, edad_txt, genero, avatar = row
                        edad = int(edad_txt)
                        self._usuarios.append(Usuario(nombre, edad, genero, avatar))
                    except (ValueError, IndexError):
                        continue
        except FileNotFoundError:
            self._cargar_datos_de_ejemplo()