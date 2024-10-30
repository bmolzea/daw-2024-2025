nTerminos = int(input("¿Cuántos términos quieres?"))
i = 1

while i<=nTerminos:
    if i == 1:
        terminoAnterior = 0
        print(terminoAnterior)

    if i == 2:
        terminoActual = 1
        print(terminoActual)

    if i >= 3:
        nuevoTermino = terminoAnterior+terminoActual
        print(nuevoTermino)
        terminoAnterior = terminoActual
        terminoActual = nuevoTermino    

    i = i + 1