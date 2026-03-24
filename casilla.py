# Creo la clase Casilla
class Casilla:
    def __init__(self):
        # Defino con estado a nave y a visitada
        self.nave = None
        self.visitada = False

    # Creo el metodo para saber si ya se habia disparado a esa casilla antes
    def disparar(self):
        if self.visitada:       # Si visitada es False
            print("Ya has disparado a esta casilla.")
            return None         # Devuelve que esa casilla ya habia sido disparada

        self.visitada = True    # Cambiamos el estado

        # Hacemos un condicional para que muestre el estado del lanzamiento
        if self.nave is None:
            print("Agua")
            return 0
        else:
            resultado = self.nave.recibir_disparo()
            if resultado == 2:
                print(f"{self.nave.nombre} Hundido")
            else:
                print(f"{self.nave.nombre} Tocado")
            return resultado