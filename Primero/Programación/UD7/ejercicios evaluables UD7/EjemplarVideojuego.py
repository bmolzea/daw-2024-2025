"""
Ejercicio 8. Crea la clase EjemplarVideojuego que herede de Videojuego. Además de los atributos de Videojuego tendrá los siguientes atributos: id (int) un número único que identifica a cada ejemplar y estado (int) un número entero entre 1 y 5 que identifica el estado de conservación del ejemplar (1 → precintado, 2 → como nuevo, 3 → ligeros desperfectos, 4 → desperfectos grandes y 5 → sin caja y/o manual).
Implementa los siguientes métodos:
__eq__ → dos ejemplares son iguales sin comparten id (en principio no tiene sentido que existan dos objetos iguales)
__str__ → mostrará por pantalla todos los atributos de la clase
__gt__, __ge__, __le__ y __lt__ → diremos que un juego es mayor/menor que otro según su estado de conservación, a mejor estado mayor será el juego.
estado_str() -> str: devuelve una cadena de texto con el estado del juego

"""

from Videojuego import Videojuego
from datetime import datetime

class EjemplarVideojuego(Videojuego):
    def __init__(self,  nombre: str, fecha_salida: datetime, puntuacion: float, generos: list, id: int, estado: int):
        super().__init__(nombre, fecha_salida, puntuacion, generos)

        self.id = id
        if estado < 1:
            estado = 1
        elif estado > 5:
            estado = 5

        self.estado = estado

    def __str__(self) -> str:
        return (super().__str__() +
                f"\nID del ejemplar: {self.id}\n"
                f"Estado: {self.estado_str()}")

    def __eq__(self, other)->bool:
        if isinstance(other, EjemplarVideojuego):
            return self.id == other.id
        return False

    def __gt__(self, other)->bool:
        return self.estado < other.estado

    def __ge__(self, other)->bool:
        return self.estado <= other.estado

    def __le__(self, other)->bool:
        return self.estado >= other.estado

    def __lt__(self, other)->bool:
        return self.estado > other.estado

    def estado_str(self) -> str:
        if self.estado == 1:
            return "Precintado"
        elif self.estado == 2:
            return "Como nuevo"
        elif self.estado == 3:
            return "Ligeros desperfectos"
        elif self.estado == 4:
            return "Desperfectos grandes"
        else:
            return "Sin caja y/o manual"