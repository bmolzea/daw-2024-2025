import random

def generarCarta() -> str:
    paloCodigo  = random.randint(1, 4)
    if paloCodigo == 1:
        palo = "oros"
    elif paloCodigo == 2:
        palo = "espadas"
    elif paloCodigo == 3:
        palo = "copas"
    elif paloCodigo == 4:
        palo = "bastos"

    numero = str(random.randint(1, 13))

    if numero == "11":
        numero = "sota"
    elif numero == "12":
        numero = "caballo"
    elif numero == "13":
        numero = "rey"
    
    carta = numero + " de " + palo
    #otra forma carta = f"{numero} de {palo}"
    return carta

i = 1

cartaElegida = input("Elige una carta (sota de bastos): ")
while True:
    cartaSacada = generarCarta()
    print(f"Carta {i}: {cartaSacada}")
    if cartaElegida == cartaSacada:
        break
    
    i += 1

print(f"Has sacado {i} cartas")