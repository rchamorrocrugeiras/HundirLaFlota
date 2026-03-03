class Nave:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.vida = tamano

    def recibir_disparo(self):
        self.vida -= 1
        0 = "Agua"
        1 = "Tocado"
        2 = "Hundido"
        return 2 if self.vida == 0 else 1