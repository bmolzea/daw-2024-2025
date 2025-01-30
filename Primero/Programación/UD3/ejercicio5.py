import math

while True:
    try:
        num = int(input("Inserte un numero:   "))
    except ValueError as error:
        print(f"Insertaste algo incorecto {error}")
    else:
        if num > 0:
            raiz_cuadrada = math.sqrt(num)
            print(f"la raiz cuadrada de {num} es {raiz_cuadrada}")
        else:
            print("FIN")
            break