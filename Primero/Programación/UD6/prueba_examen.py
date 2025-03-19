from Videojuego2 import Videojuego2
from datetime import datetime

# Forma guay
def e1a(videojuegos: list) -> Videojuego2:
    max_puntuacion = max([juego.puntuacion for juego in videojuegos])
    return [juego for juego in videojuegos if juego.puntuacion == max_puntuacion][0]

# Forma menos guay
def e1a2(videojuegos: list) -> Videojuego2:
    max_puntuacion = videojuegos[0].puntuacion
    max_juego = videojuegos[0]
    for juego in videojuegos:
        if juego.puntuacion > max_puntuacion:
            max_puntuacion = juego.puntuacion
            max_juego = juego
    return max_juego

# Forma moderna
def e1b(videojuegos: list) -> Videojuego2:
    rpgs = [juego for juego in videojuegos if "RPG" in juego.generos]
    max_puntuacion = max([juego.puntuacion for juego in rpgs])
    return [juego for juego in rpgs if juego.puntuacion == max_puntuacion][0]

# Forma 1990
def e1b2(videojuegos: list) -> Videojuego2:
    rpgs = [juego for juego in videojuegos if "RPG" in juego.generos]
    max_puntuacion = rpgs[0].puntuacion
    max_juego = rpgs[0]
    for juego in rpgs:
        if juego.puntuacion > max_puntuacion:
            max_puntuacion = juego.puntuacion
            max_juego = juego
    return max_juego

# Forma guay
def e1c(videojuegos: list) -> list:
    return [juego for juego in videojuegos if juego.fecha_salida.month>= 1 and juego.fecha_salida.month<= 6]

# Forma 1800
def e1c2(videojuegos: list) -> list:
    juegos_primeros_meses = []
    for juego in videojuegos:
        if juego.fecha_salida.month >= 1 and juego.fecha_salida.month <= 6:
            juegos_primeros_meses.append(juego)
    return juegos_primeros_meses

# Forma moderna
def e1d(videojuegos: list) -> list:
    return [juego for juego in videojuegos if len(juego.generos) >= 3]
            
# Forma 1700
def e1d2(videojuegos: list) -> list:
    juegos_mas_tres_generos = []
    for juego in videojuegos:
        if  len(juego.generos) >= 3:
            juegos_mas_tres_generos.append(juego)
    return juegos_mas_tres_generos

juegos = [
   Videojuego2("Final Fantasy VI", ["RPG"], datetime(1994, 4, 2), 9.5, 12, 49.99, 0.5),
   Videojuego2("The Legend of Zelda: Ocarina of Time", ["Aventura", "Acción"], datetime(1998, 11, 11), 9.9, 12, 39.99, 0.8),
   Videojuego2("Grand Theft Auto: San Andreas", ["Acción", "Mundo Abierto"], datetime(2004, 10, 3), 9.6, 18, 29.99, 4.7),
   Videojuego2("The Elder Scrolls V: Skyrim", ["RPG", "Mundo Abierto"], datetime(2011, 11, 3), 9.7, 18, 59.99, 12),
   Videojuego2("The Last of Us", ["Acción", "Aventura"], datetime(2013, 6, 14), 9.8, 18, 39.99, 45),
   Videojuego2("Bloodborne", ["Acción", "Souls-like"], datetime(2015, 3, 1), 9.7, 18, 19.99, 41),
   Videojuego2("The Legend of Zelda: Breath of the Wild", ["Aventura", "Mundo Abierto"], datetime(2017, 3, 3), 10, 12, 59.99, 13.4),
   Videojuego2("Red Dead Redemption 2", ["Acción", "Mundo Abierto"], datetime(2018, 10, 26), 9.9, 18, 59.99, 120),
   Videojuego2("Elden Ring", ["RPG", "Acción", "Souls-like"], datetime(2022, 2, 25), 9.8, 16, 59.99, 60),
   Videojuego2("Final Fantasy VII Rebirth", ["RPG", "Acción"], datetime(2025, 2, 10), 9.7, 16, 69.99, 100)
]

print(e1a(juegos).nombre)
print(e1a2(juegos).nombre)
print(e1b(juegos).nombre)
print(e1b2(juegos).nombre)

# Version 1990
print("Los juegos que salieron en los primeros 6 meses del año son: ")
juegos_primeros_meses = e1c(juegos)
for juego in juegos_primeros_meses:
    print(juego.nombre)

# Version moderna
print([juego.nombre for juego in e1c(juegos)])

print([juego.nombre for juego in e1d(juegos)])
print([juego.nombre for juego in e1d2(juegos)])