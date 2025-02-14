palabras = []
while True:
    n = input("Inserta un número: ")
    if n == "fin":
        break
    else:
        palabras.append(n)

palabras.sort()
print(palabras)