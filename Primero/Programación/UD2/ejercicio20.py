lado1 = float(input("Inserta la longitud del lado 1: "))
lado2 = float(input("Inserta la longitud del lado 2: "))
lado3 = float(input("Inserta la longitud del lado 3: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("El triángulo es válido")
else:
    print("El triángulo no es válido")