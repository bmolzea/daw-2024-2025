from EjemplarLibro import EjemplarLibro
from datetime import datetime


l1 = EjemplarLibro("348938403-349", "El Señor de los anillos", ["Tolkien"], ["Aventura", "Ficción"], 40560, 15, "Tapa dura", "Borgasa", 645, [8, 15], "38293828309280", 2, 2, False)

l2 = EjemplarLibro("3484588403-567", "El Señor de los anillos", ["Tolkien"], ["Aventura", "Ficción"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293828309280", 1, 0, False)

l3 = EjemplarLibro("3489659403-119", "El Quijote", ["Cervantes"], ["Aventura", "Caballería"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293828309280", 3, 1, True, datetime(2025, 3, 30), datetime(2025, 4, 15), "75584525J")

libros = [l1, l2, l3]

# for ejemplar in libros:
#     print(ejemplar)

# Seleccionamos los libros que son nuevos o como nuevos
nuevo_como_nuevo = [libro for libro in libros if libro.estado == 1 or libro.estado == 2]
print("Libros que están nuevos o como nuevos:")
for libro in nuevo_como_nuevo:
    print(libro)

# Se imprimen los libros prestados
print("\n\nLibros que están prestados:")
for libro in libros:
    if libro.prestado:
        print(f"Título: {libro.titulo}, Código de barras: {libro.codigo_barras}")

