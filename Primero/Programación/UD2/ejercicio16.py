lado1 = float(input("Inserta la longitud del lado 1: "))
lado2 = float(input("Inserta la longitud del lado 2: "))
lado3 = float(input("Inserta la longitud del lado 3: "))

if lado1 == lado2  == lado3:
    print("Equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Isósceles")
else:
    print("Escaleno")