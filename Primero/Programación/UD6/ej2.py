from Videojuego import Videojuego

videojuegos = [
    Videojuego("The Witcher III", ["RPG", "Acción", "Aventura"], "2015-05-19",9.7, 18, 39.99, 50),
    Videojuego("Grand Theft Auto V", ["Acción", "Mundo Abierto"], "2013-09-17", 9.5, 18, 29.99, 95),
   Videojuego("Zelda: Breath of the Wild", ["Aventura", "Mundo Abierto"], "2017-03-03", 10.0, 12, 59.99, 13.4),
   Videojuego("Minecraft", ["Supervivencia", "Sandbox"], "2011-11-18", 9.0, 7, 26.95, 1.2),
   Videojuego("Red Dead Redemption 2", ["Acción", "Mundo Abierto"], "2018-10-26", 9.8, 18, 59.99, 150),
   Videojuego("God of War (2018)", ["Acción", "Aventura"], "2018-04-20", 9.6, 18, 49.99, 45),
   Videojuego("Dark Souls III", ["RPG", "Acción", "Souls-like"], "2016-04-12", 9.3, 16, 39.99, 25),
   Videojuego("Animal Crossing: New Horizons", ["Simulación", "Social"], "2020-03-20", 9.1, 3, 49.99, 10.02),
   Videojuego("Cyberpunk 2077", ["RPG", "Mundo Abierto"], "2020-12-10", 8.5, 18, 59.99, 70),
   Videojuego("Super Mario Odyssey", ["Plataformas", "Aventura"], "2017-10-27", 9.8, 7, 49.99, 5.6)
]

# Opción 1
juegos_filtrados = [juego for juego in videojuegos if juego.apto_menores() and juego.puntuacion >= 9 and juego.peso < 50]

# Opción 2
"""
def filtrar(juego: Videojuego) -> bool:
    return juego.apto_menores() and juego.puntuacion >= 9 and juego.peso < 50

juegos_filtrados = [juego for juego in videojuegos if filtrar(juego)]

del filtrar"
"""

print("Los juegos que cumplen el filtro son:")
for juego in juegos_filtrados:
    print(juego.nombre)