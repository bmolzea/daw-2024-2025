from datetime import datetime
from EjemplarLibro import EjemplarLibro
from Biblioteca import Biblioteca

# Para fines estéticos para separar de forma evidente distintas secciónes 
def mostrar_separador():
    print("\n#####################\n")

libros = [
    EjemplarLibro("348938403-349", "El Señor de los anillos", ["Tolkien"], ["Aventura", "Ficción"], 40560, 15, "Tapa dura", "Borgasa", 645, [8, 15], "38293828309280", 2, 2, False),
    EjemplarLibro("3484588403-567", "El Señor de los anillos", ["Tolkien"], ["Aventura", "Ficción"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293828309280", 1, 0, False),
    EjemplarLibro("3489659403-119", "El Quijote", ["Cervantes"], ["Aventura", "Caballería"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293844909280", 3, 1, True, datetime(2025, 3, 30), datetime(2025, 4, 15), "75584525J"),
    EjemplarLibro("3489659403-119", "El Quijote", ["Cervantes"], ["Aventura", "Caballería"], 40560, 15, "Tapa blanda", "Borgasa", 645, [8, 15], "38293844909281", 3, 1, True, datetime(2025, 3, 1), datetime(2025, 3, 30), "75584541K"),
]

biblioteca = Biblioteca(libros)

# Imprimimos todos los ejemplares
print(biblioteca)

mostrar_separador()

# Mostramos solo los ejemplares disponibles
biblioteca.mostrar_disponibles()

mostrar_separador()

# Mostramos los ejemplares prestados
biblioteca.mostrar_prestados()

mostrar_separador()

# Mostramos los distintos libros que componen nuestra biblioteca sin mostrar repeticiones, es decir si tenemos varios ejemplares del Quijote de varias ediciones solo mostramos una vez el Quijote
biblioteca.mostrar_libros_distintos()

mostrar_separador()

# Quitamos El Señor de los Anillos de tapa blanda de nuestra biblioteca y comprobamos que ya no lo tenmos
biblioteca.quitar_libro("38293828309280")
print(biblioteca)

mostrar_separador()

# Mostrarmos los libros que deberían haber sido devueltos y aún los tiene alguien
biblioteca.mostrar_devoluciones_atrasadas()