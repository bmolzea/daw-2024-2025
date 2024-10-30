factorial = int(input("Inserta un número: "))
i = 2
resultado = 1

while i <= factorial:
    resultado = resultado * i
    i = i + 1

print(f"El factorial de {factorial} es: {resultado}")