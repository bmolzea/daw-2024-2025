from EjemplarLibro import EjemplarLibro
from Libreria import Libreria
from datetime import datetime


l1 = EjemplarLibro("348938403-349", "El Señor de los anillos", ["Tolkien"], ["Aventura", "Ficción"], 40560, 15, "Tapa dura", "Borgasa", 645, [8, 15], "38293828309280", 2, 2, False)

l2 = EjemplarLibro("3484588403-567", "El Señor de los anillos", ["Tolkien"], ["Aventura", "Ficción"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293828309280", 1, 0, False)

l3 = EjemplarLibro("3489659403-119", "El Quijote", ["Cervantes"], ["Aventura", "Caballería"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293828309280", 3, 1, True, datetime(2025, 3, 30), datetime(2025, 4, 15))

libreria = Libreria([l1, l2, l3])

print(libreria)