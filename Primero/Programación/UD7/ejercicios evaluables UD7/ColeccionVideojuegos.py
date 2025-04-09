"""Ejercicio 9. Crea la clase ColeccionVideojuegos cuyo único atributo será una lista de objetos de la clase EjemplarVideojuego. Implementa los siguientes métodos:
__str__ → muestra por pantalla todos los juegos que tenga la colección, solo se debe mostrar el nombre y el estado (como cadena de texto)
juegos_repetidos() -> list<Videojuego>: devuelve una lista con los Videojuegos de la colección de los cuales se tengan varios ejemplares
mostrar_juegos_repetidos(): muestra por pantalla el nombre de los videojuegos que estén repetidos
eliminar_juego(id: int): elimina mediante su id un videojuego de la colección

"""
from Videojuego import Videojuego
from  EjemplarVideojuego import EjemplarVideojuego

class ColeccionVideojuegos:

    def __init__(self, coleccion: list[EjemplarVideojuego]):
        self.coleccion = coleccion

    def __str__(self)->str:
        coleccion_str = "La colección completa es:\n"

        for videojuego in self.coleccion:
            coleccion_str += (f"Nombre: {videojuego.nombre}\n"
                              f"Estado: {videojuego.estado_str()}\n"
                              f"{'-' * 40}\n")
        return coleccion_str

    def juegos_repetidos(self) -> list[Videojuego]:
        
        def comparar(j1: EjemplarVideojuego, j2: EjemplarVideojuego) -> bool:
            return j1.nombre == j2.nombre and j1.fecha_salida == j2.fecha_salida
        
        def contiene(juego: EjemplarVideojuego, juegos: list) -> bool:
            lo_contiene = False
            for j in juegos:
                if comparar(juego, j):
                    lo_contiene = True
                    break
            return lo_contiene
        
        
        repetidos = []
        no_repetidos = []

        for j in self.coleccion:
            if not contiene(j, no_repetidos):
                no_repetidos.append(j)
            else:
                if not contiene(j, repetidos):
                    repetidos.append(j)
       
        return repetidos

    def mostrar_juegos_repetidos(self):
        repetidos = self.juegos_repetidos()

        if repetidos:
            print("Los juegos repetidos son: ")

            for juego in repetidos:
                print(juego.nombre)
        else:
            print("No hay juegos repetidos")

    def eliminar_juego(self, id: int):
        juegos_iniciales = len(self.coleccion)
        self.coleccion = [juego for juego in self.coleccion if juego.id != id]

        if len(self.coleccion) < juegos_iniciales:
            print("Juego(s) eliminado(s) correctamente")
        else:
            print("No se encontró el juego")




