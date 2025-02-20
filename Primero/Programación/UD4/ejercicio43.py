"""
Crea una lista con palabras. Crea una segunda lista que contenga las mismas palabras pero con todas sus letras en mayúscula.

"""

palabras = ["abejorro", "perro", "gato", "abaco"]

palabras_mayus = [palabra.upper() for palabra in palabras]

print(palabras_mayus)