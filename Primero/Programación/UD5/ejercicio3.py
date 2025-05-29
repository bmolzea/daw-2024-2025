texto = input("Introduce un texto: ")
palabras = texto.split()

n_veces = {}
for palabra in palabras:
    if palabra in n_veces:
        n_veces[palabra] += 1
    else:
        n_veces[palabra] = 1

print("\nFrecuencia de palabras:")
for palabra in n_veces:
    print(f"{palabra}: {n_veces[palabra]}")