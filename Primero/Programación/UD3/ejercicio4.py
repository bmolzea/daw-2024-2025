#Crea un programa que lea números hasta que se introduzca un 0. El programa deberá calcular la media aritmética de todos los números insertados, el número máximo y el número mínimo. 
num_veces = 0
num_total = 0
num_min = 0
num_max = 0
while True:
    try:
        num = int(input("inserta un numero (0 para salir )"))
    except ValueError as error:
        print(f"introduce un numero  {error}")
    except Exception as error:
        print(f"{error}")
    else:
        if num == 0:
            break
        num_total = num_total+num
        num_veces += 1
        if num_max < num:
            num_max = num
        if num_min > num or num_min == 0:
            num_min = num
media = num_total / num_veces
print(f"la media es:{media}")
print(f"el numero maximo es: {num_max} y el numero minimo es: {num_min}")

    


