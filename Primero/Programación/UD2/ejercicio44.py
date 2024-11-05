while True:
    num = float(input("Inserta un número: "))
    if num == 0:
        break
    cifras = int(input("Inserta el número de cifras al que quieres redondear: "))
    numRedondeado = round(num, cifras)
    print(f"El número {num} redondeado a {cifras} cifras es: {numRedondeado}")