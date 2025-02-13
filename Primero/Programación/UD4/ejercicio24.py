"""Crea un programa que inserte números en una lista hasta introducir el número 0. A continuación deberá mostrar en pantalla todos los números introducidos en orden inverso, es decir primero el último número introducido. 
"""

nums = []

while True:
    n = int(input("Inserta un número: "))
    if n == 0:
        break
    nums.append(n)

print("La lista en orden inverso:")
for _ in range(len(nums)):
    print(nums.pop())