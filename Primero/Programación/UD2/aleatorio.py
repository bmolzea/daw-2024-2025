import random

def lanzarMoneda():
    tirada = random.random()
    if tirada <= 0.5:
        print("Cara")
    else:
        print("Cruz")

def lanzarMonedas(nMonedas: int):
    for _ in range(nMonedas):
        lanzarMoneda()

def lanzarDado():
    tirada = random.randint(1, 6)
    print(tirada)

def lanzarDados(nDados: int):
    for _ in range(nDados):
        lanzarDado()

