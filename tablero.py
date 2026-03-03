class Tablero:
    def __init__(self, filas=10, columnas=10):
        self.matriz = [["~"] * columnas for _ in range(filas)]
        self.naves = []

    def colocar_nave(self, nave, fila, columna, horizontal=True):
        for i in range(nave.vida):
            if horizontal:
                self.matriz[fila][columna + i] = nave
            else:
                self.matriz[fila + i][columna] = nave
        self.naves.append(nave)

    def comprobar_impacto(self, fila, columna):
        celda = self.matriz[fila][columna]
        if isinstance(celda, object) and celda != "~":
            resultado = celda.recibir_disparo()
            self.matriz[fila][columna] = "X"
            return resultado, celda.nombre
        0 = "Agua"
        1 = "Tocado"
        2 = "Hundido"
        return 0, None