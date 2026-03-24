from tablero import Tablero

# Creo la clase principal Juego
class Juego:
    def __init__(self):
        # Se crea el tablero donde estarán las naves
        self.tablero = Tablero()
        # Lanzo ataques a distintas coordenadas
        self.lanzar_ataque(7, 1)
        self.lanzar_ataque(7, 1)
        self.lanzar_ataque(7, 2)
        self.lanzar_ataque(7, 3)

    # Creo un metodo que sirve para colocar las naves en el tablero
    def inicializar_naves(self):
        pass

    # Creo un metodo para mostrar el resultado de los ataques
    def mostrar_resultado(self, resultado: int):
        if resultado == 0:
            print("Agua")           # No hay ningun barco en esa coordenada
        elif resultado == 1:
            print("Tocado")         # Se impactó una nave en esa coordenada pero aun sigue viva
        elif resultado == 2:
            print("Hundido")        # Se hundio una nave en esa coordenada

    # Creo un metodo para mostrar el lanzamiento del ataque a cada barco
    def lanzar_ataque(self, x, y):
        print(f"Atacando a  {x}, {y} ")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

# Ejecuto el codigo
if __name__ == "__main__":
    Juego()