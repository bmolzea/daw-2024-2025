num = int(input("Inserta un número: "))

esPrimo = True
for i in range(2, num):
    if num % i == 0:
        esPrimo = False
        break

if esPrimo:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} NO es primo")