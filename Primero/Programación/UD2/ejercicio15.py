print("¿Qué quieres calcular?")
print("1. Triángulo")
print("2. Rectángulo")
print("3. Circunferencia")
opcion = int(input("Elige una opción: "))

if opcion == 1:
    base = float(input("Inserta la base: "))
    altura = float(input("Inserta la altura: "))
    area = base * altura / 2
    print(f"El área de un triángulo de base {base} y altura {altura} es {area}")
elif opcion == 2:
    base = float(input("Inserta la base: "))
    altura = float(input("Inserta la altura: "))
    area = base * altura
    print(f"El área de un rectángulo de base {base} y altura {altura} es {area}")
elif opcion == 3:
    radio = float(input("Inserta el radio: "))
    pi = 3.1416
    area = pi * radio * radio
    print(f"El área de una circunferencia de radio {radio} es {area}")