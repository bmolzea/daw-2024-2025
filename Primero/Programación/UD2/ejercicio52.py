import random
def caraCruz(nVeces: int):
    for i in range(nVeces):
        num = random.randint(0, 1)
        if num == 0:
            print("Cara")
        else:
            print("Cruz")

nVeces = int(input("Cuántas monedas quieres lanzar: "))
caraCruz(nVeces)