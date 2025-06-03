texto = input("Introduce un texto: ")

diccionario = {}

palabras = texto.split()

for palabra in palabras:
    if palabra not in diccionario:
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

for palabra, contador in diccionario.items():
    print(f"{palabra} : {contador}")
