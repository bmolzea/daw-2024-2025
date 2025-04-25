from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bonsai:
    Nombre:str
    Delicadeza:int
    AlturaMediaCM:int
    FechaPoda:datetime
    Plagas:list[str]

def leer_bonsai(atributos:list[str])->list[Bonsai]:
    fecha = atributos[3].split("/")
    fecha = datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
    plagas = atributos[4].split("-")
    return Bonsai(
        atributos[0],
        int(atributos[1]),
        int(atributos[2]),
        fecha,
        plagas
    )

bonsais = []
with open ("bonsais.csv","r",encoding="utf-8") as f:
    contador_linea = 1
    for linea in f:
        if contador_linea>1:
            atributos = linea.strip().split(",")
            bonsais.append(leer_bonsai(atributos))
        contador_linea += 1

print("Los bonsais que hay son:")
for b in bonsais:
    print(b)

print("los bonsais que pueden ser atacados por los pulgones son: ")
for b in bonsais:
    if "Pulgón" in b.Plagas:
        print(f"- {b.Nombre}\n")
        