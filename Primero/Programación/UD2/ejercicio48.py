import random

inicio = float(input("Inserta el límite inferior: "))
fin = float(input("Inserta el límite superior: "))
nVeces = int(input("Inserta la cantidad de números aleatorios a generar: "))

for i in range(nVeces):
   numAleatorio = round(inicio + (fin-inicio)*random.random(), 2)
   print(numAleatorio)