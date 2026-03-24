# Actividad: Hundir la Flota en Python

### 1. Realizamos ataques a las coordenadas (7,1), (7,1), (7,2), (7,3)
```commandline
self.lanzar_ataque(7, 3)
self.lanzar_ataque(7, 1)
self.lanzar_ataque(7, 1)
self.lanzar_ataque(7, 2)
```
### 2. Se ejecuta el método *lanzar_ataque*
### 3. Comprueba si ya se había disparado a esa casilla
### 4. Si impactó en alguna nave se le descuenta una vida
### 5. Se muestra el estado de la nave
    AGUA
    TOCADO
    HUNDIDO
### Una vez se haya realizado esto es lo que se nos muestra por pantalla:
```commandline
Atacando a  7, 1 
[LOG] estoy en tablero comprobando impacto (7, 1)
[LOG] Vidas restantes de Prince of Wales: 2
[LOG] Prince of Wales Tocado
Tocado
Atacando a  7, 1 
[LOG] estoy en tablero comprobando impacto (7, 1)
[LOG] Ya has disparado a esta casilla
Atacando a  7, 2 
[LOG] estoy en tablero comprobando impacto (7, 2)
[LOG] Vidas restantes de Prince of Wales: 1
[LOG] Prince of Wales Tocado
Tocado
Atacando a  7, 3 
[LOG] estoy en tablero comprobando impacto (7, 3)
[LOG] Vidas restantes de Prince of Wales: 0
[LOG] Nave hundida
[LOG] Prince of Wales Hundido
Hundido

Process finished with exit code 0
```