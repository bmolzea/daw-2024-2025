num_secreto = 42
n_intentos = 1

while True:
    try:
        num = int(input("Inserta un número"))
    except Exception as error:
        print("Se ha producido un error")
    else:
        if num == num_secreto:
            print(f"Acertaste!!! en {n_intentos} intentos")
            break
        elif num < num_secreto:
            print("El num secreto es mayor")
        else:
            print("El num secreto es menor")
        
        n_intentos += 1
        
