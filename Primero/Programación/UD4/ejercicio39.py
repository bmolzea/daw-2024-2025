palabras = input("Inserta palabras separadas por comas: ").split(",")
menor = palabras[0]
mayor = palabras[0]

for palabra in palabras:
    if len(palabra) > len(mayor):
        mayor = palabra
    if len(palabra) < len(menor):
        menor = palabra