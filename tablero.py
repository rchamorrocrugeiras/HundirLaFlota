class Tablero:
    def __init__(self):
        self.posiciones = {}

    def colocar_nave(self, x, y, nave):
        self.posiciones[(x, y)] = nave