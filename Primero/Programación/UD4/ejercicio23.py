"""Crea un programa que permita insertar números naturales* en una lista.  Cada vez que insertes un número deberá mostrar la lista entera. Si se inserta un número negativo deberá eliminar la primera aparición de su análogo positivo de la lista, es decir si inserto -3 lo que significa es “elimina el primer tres insertado”
"""
nums = []

while True:
    n = int(input("Inserta un número: "))

    if n == 0:
        break
    elif n > 0:
        nums.append(n)
    else:
        if n*-1 in nums:
            nums.remove(n*-1)
    
    print(nums)