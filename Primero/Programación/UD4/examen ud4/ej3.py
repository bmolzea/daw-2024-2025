from random import randint

def emparejar(bombo1: list, bombo2: list):
    n_emparejamientos = len(bombo1)
    for _ in range(n_emparejamientos):
        equipo1 = bombo1[randint(0, len(bombo1)-1)]
        equipo2 = bombo2[randint(0, len(bombo2)-1)]
        bombo1.remove(equipo1)
        bombo2.remove(equipo2)
        print(f"{equipo1} vs {equipo2}")

equipos1 = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Bilbao"]
equipos2 = ["Real Sociedad", "Betis", "Granada", "Valencia"]
print("ENFRENTAMIENTOS:")
emparejar(equipos1.copy(), equipos2.copy())