numSecreto = 45
nIntentos = 1
haAcertado = False

while not haAcertado:
    numSeleccionado = int(input("Inserta un número: "))
    
    if numSeleccionado == numSecreto:
        print(f"Has acertado! con {nIntentos} intentos")
        haAcertado = True
    elif numSeleccionado < numSecreto:
        print("Ese no es! Es mayor!")
    else:
        print("Ese no es! Es menor!")

    nIntentos = nIntentos + 1