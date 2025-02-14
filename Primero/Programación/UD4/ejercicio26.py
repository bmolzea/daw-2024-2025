"""Crea un programa que inserte números en una lista. Si el número ya existe en la lista NO debe volver a introducirlo, de tal forma que la lista no contenga número repetidos:
"""
nums = []
while True:
    n = int(input("Inserta un número: "))
    if nums.count(n) == 0:
        nums.append(n)
    else:
        print("El número ya está en la lista")
    print(f"Contenido de la lista: {nums}")
