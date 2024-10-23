print("¿Qué quieres calcular?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = input()

num1 = int(input("Introduce el primer número"))
num2 = int(input("Introduce el segundo número"))

match opcion:
    case "1":
        print(f"{num1} + {num2} = {num1+num2}")
    case "2":
        print(f"{num1} - {num2} = {num1-num2}")
    case "3":
        print(f"{num1} * {num2} = {num1*num2}")
    case "4":
        print(f"{num1} / {num2} = {num1/num2}")
