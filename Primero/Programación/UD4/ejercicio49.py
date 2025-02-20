matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

mas_letras = matriz[0][0]

for fila in matriz:
    for animal in fila:
        if len(mas_letras) < len(animal):
            mas_letras = animal

print(f"El animal con más letras es: {mas_letras}")

