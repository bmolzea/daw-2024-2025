while True:
    print("¿Qué operación quieres realizar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Divsión")
    print("5. División entera")
    print("6. Módulo")
    print("Inserta 'fin' para terminar")
    
    opcion = input("¿Qué quieres hacer?")

    if opcion == "fin":
        break

    num1 = int(input("Inserta el primer número: "))
    num2 = int(input("Inserta el segundo número: "))

    match opcion:
        case "1":
            print(f"{num1} + {num2} = {num1+num2}")
        case "2":
            print(f"{num1} - {num2} = {num1-num2}")
        case "3":
            print(f"{num1} * {num2} = {num1*num2}")
        case "4":
            print(f"{num1} / {num2} = {num1/num2}")
        case "5":
            print(f"{num1} // {num2} = {num1//num2}")
        case "6":
            print(f"{num1} % {num2} = {num1%num2}")

   