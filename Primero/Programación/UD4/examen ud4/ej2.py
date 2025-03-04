animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]
pesos_animales = [
    [5, 40],   # Perro (depende de la raza)
    [2, 8],    # Gato
    [1, 3],    # Conejo
    [0.08, 0.25], # Hámster
    [0.2, 1.5],   # Loro
    [0.1, 2],  # Pez (varía mucho según la especie)
    [0.5, 2],  # Tortuga (pequeñas domésticas)
    [0.7, 1.5],  # Cobaya
    [0.5, 2],  # Hurón
    [0.02, 0.06] # Canario
]

# Forma tradicional (con bucles y condicionales)
max_dif = 0
pos_max_dif = 0
n_animales = len(animales_domesticos)
for i in range(n_animales):
    dif = pesos_animales[i][1] - pesos_animales[i][0]
    if dif > max_dif:
        max_dif = dif
        pos_max_dif = i
animal_mayor_dif = animales_domesticos[pos_max_dif]
print(f"El animal cuya diferencia entre peso máximo y mínimo es mayor es el {animal_mayor_dif} con una diferencia de {max_dif}kg")

# Usando list comprehensions y funciones auxiliares
diferencias = [pesos[1]-pesos[0] for pesos in pesos_animales]
max_dif = max(diferencias)
pos_mayor_dif = diferencias.index(max_dif)
animal_mayor_dif = animales_domesticos[pos_mayor_dif]
print(f"El animal cuya diferencia entre peso máximo y mínimo es mayor es el {animal_mayor_dif} con una diferencia de {max_dif}kg")