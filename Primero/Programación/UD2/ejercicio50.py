import random

def jugadaBot() -> str:
    numeroJugada = random.randint(1, 3)
    if numeroJugada == 1:
        jugada = "Piedra"
    elif numeroJugada == 2:
        jugada = "Papel"
    elif numeroJugada == 3:
        jugada = "Tijera"

    return jugada

def ganador(jugadaHumano: str, jugadaBot: str) -> int:
    resultado = 0
    if jugadaHumano == "Piedra":
        if jugadaBot == "Tijera":
            resultado = 1
        elif jugadaBot == "Papel":
            resultado = -1
    elif jugadaHumano == "Tijera":
        if jugadaBot == "Piedra":
            resultado = -1
        elif jugadaBot == "Papel":
            resultado = 1
    elif jugadaHumano == "Papel":
        if jugadaBot == "Piedra":
            resultado = 1
        elif jugadaBot == "Tijera":
            resultado = -1
    return resultado

puntosHumano = 0
puntosBot = 0
ronda = 1

while puntosHumano<3 and puntosBot<3:
    print(f"=== RONDA {ronda} ===")
    jugada1 = input("¿Qué jugada quieres hacer? ")
    jugada2 = jugadaBot()
    print(f"El bot ha elegido: {jugada2}")
    resultado = ganador(jugada1, jugada2)
    if resultado == 1:
        print("Has ganado")
        puntosHumano = puntosHumano + 1
    elif resultado == 0:
        print("Empate")
    elif resultado == -1:
        print("Has perdido")
        puntosBot = puntosBot + 1
    
    ronda = ronda + 1
    print(f"Humano: {puntosHumano} puntos")
    print(f"Bot: {puntosBot} puntos")