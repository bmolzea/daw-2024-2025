from Videojuego import Videojuego

juegos_borja = [
   Videojuego("Dark Souls III", ["RPG", "Acción", "Souls-like"], "2016-04-12", 9.3, 16, 39.99, 25),
   Videojuego("Bloodborne", ["RPG", "Acción", "Souls-like"], "2015-03-24", 9.7, 18, 19.99, 41),
   Videojuego("Elden Ring", ["RPG", "Acción", "Souls-like"], "2022-02-25", 9.8, 16, 59.99, 60),
   Videojuego("Sekiro: Shadows Die Twice", ["Acción", "Souls-like"], "2019-03-22", 9.5, 18, 49.99, 25),
   Videojuego("Lies of P", ["RPG", "Acción", "Souls-like"], "2023-09-19", 9.0, 16, 59.99, 35)
]

for v in juegos_borja:
    print(v)

