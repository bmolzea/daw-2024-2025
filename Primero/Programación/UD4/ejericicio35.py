"""
Crea un programa que lea números hasta que insertes un cero. Una vez se inserte el cero se mostrarán los números introducidos de mayor a menor (el cero no debe contar). 
"""

nums = []
while True:
    n = int(input("Inserta un número: "))
    if n == 0:
        break
    else:
        nums.append(n)

nums.sort()
nums.reverse()
print(nums)