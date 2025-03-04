animales_domesticos = ["Perro", "Gato", "Conejo", "Colibrí", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario", "Chinchilla"]
pesos_animales = [10, 4, 2, 0.01, 0.1, 0.3, 0.2, 1.5, 1, 1.2, 0.05, 1.2] 

# Animal de menor peso

# Forma tradicional (Solo bucles y condicionales)
pos_menor = 0
n_animales = len(animales_domesticos)
for i in range(n_animales):
    if pesos_animales[i] < pesos_animales[pos_menor]:
        pos_menor = i
peso_menor = pesos_animales[pos_menor]
animal_menor = animales_domesticos[pos_menor]
print(f"El animal que menos pesa es el {animal_menor} y pesa {peso_menor} kg")

# Utilizando los métodos de las listas
peso_menor = min(pesos_animales)
pos_menor = pesos_animales.index(peso_menor)
animal_menor = animales_domesticos[pos_menor]
print(f"El animal que menos pesa es el {animal_menor} y pesa {peso_menor} kg")


# Animales cuyo peso es superior a la media

# Sin utilizar métodos de las listas ni funciones adicionales
suma = 0
for peso in pesos_animales:
    suma += peso
n_animales = len(animales_domesticos)
media = suma / n_animales 

print("Animales cuyo peso es superior a la media: ")
for i in range(n_animales):
    if pesos_animales[i] > media:
        print(animales_domesticos[i])


# Utilizando funciones adicionales y list comprehension
media = sum(pesos_animales)/len(animales_domesticos)
animales_pesados = [animal for i, animal in enumerate(animales_domesticos) if pesos_animales[i] > media]
print(f"Animales cuyo peso es superior a la media: {animales_pesados}")
