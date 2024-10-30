altura = int(input("Inserta la altura: "))
base = int(input("Inserta la base: "))
caracter = input("Inserta el caracter: ")

# Si lo resolvemos usando +
linea = caracter
i = 1
while i < base:
    linea = linea + caracter
    i = i + 1

# Si lo resolvemos el anterior while usando * seria solo --> linea = caracter * base

i = 0
while i < altura:
    print(linea)
    i = i + 1
