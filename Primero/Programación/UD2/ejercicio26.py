numeroCorrecto = False

# Comprobamos que el usuario inserta un número mayor que cero
while not numeroCorrecto:
    num = int(input("Introduzca un número: "))
    if num>= 0:
        numeroCorrecto = True
    else:
        print("El número ha de ser positivo")

# Realizamos la cuenta atrás
while num != -1:
    print(num)
    num = num - 1
print("Ring ring")

