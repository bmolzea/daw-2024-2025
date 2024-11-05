import random

inicio = int(input("Inserta el límite inferior: "))
fin = int(input("Inserta el límite superior: "))
nVeces = int(input("Inserta la cantidad de números aleatorios a generar: "))

for i in range(nVeces):
    print(random.randint(inicio, fin))