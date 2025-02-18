"""
Crea un programa que lea números hasta que insertes un cero. Al finalizar el programa deberá mostrar:
El mayor de los números introducidos
El menor de los números introducidos
La media de los números introducidos
Utiliza las funciones que acabamos de estudiar. 
"""

nums = []
while True:
    n = int(input("Inserta un número: "))
    if n == 0:
        break
    else:
        nums.append(n)

print(f"El máximo es: {max(nums)}")
print(f"El mínimo es: {min(nums)}")
print(f"La media es: {sum(nums)/len(nums)}")