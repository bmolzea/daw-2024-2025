"""
 Crea un programa que lea números hasta que insertes un 0. Al terminar de leer números deberá mostrar por pantalla aquellos números insertados que sean superiores a la media. 
"""

nums = []
suma = 0


while True:
    n = int(input("Inserta un número: "))
    if n == 0:
        break
    nums.append(n)
    suma += n

media = suma / len(nums)

print(f"La media es: {media}")
print("Y los números mayores a la media son:")
for n in nums:
    if n > media:
        print(n)