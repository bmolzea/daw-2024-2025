
"""Ejercicio 10. Utilizando las clases de los ejercicios anteriores crea un programa
con la siguiente colección de videojuegos:
A continuación:
Muestra por pantalla todos los juegos (nombre y estado)
Muestra por pantalla los juegos repetidos (solo el nombre)
Elimina el juego cuyo id es 4
Vuelve a mostrar por pantalla los juegos repetidos
"""
from datetime import datetime
from EjemplarVideojuego import EjemplarVideojuego
from ColeccionVideojuegos import ColeccionVideojuegos


videojuegos = [
    EjemplarVideojuego("The Legend of Zelda: Breath of the Wild", datetime(2017, 3, 3), 10, ["Accion", "Aventura", "Mundo Abierto"],1, 5),
    EjemplarVideojuego("Red Dead Redemption 2", datetime(2018, 10, 26), 9.8, ["Accion", "Aventura", "Mundo Abierto"],2, 4),
    EjemplarVideojuego("Elden Ring", datetime(2022, 2, 25), 9.7, ["RPG", "Accion", "Mundo Abierto"],3, 5),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"],4, 3),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"],5, 1),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"],5, 1)
]

biblioteca = ColeccionVideojuegos(videojuegos)

#muestra por pantalla todos los videojuegos
print("Todos los juegos: ")
print(biblioteca)


#juegos repetidos
biblioteca.mostrar_juegos_repetidos()

#Elimina el juego cuyo id es 4
biblioteca.eliminar_juego(4)

#para que se vea que se ha eliminado el id = 4
print("Tras borrar el juego")
print(biblioteca)
#juegos repetidos despues de eliminar id=4
biblioteca.mostrar_juegos_repetidos()