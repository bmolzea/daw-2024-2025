from dataclasses import dataclass
from datetime import datetime

@dataclass
class Pelicula:
    titulo: str
    duracion: int
    edad_minima: int
    actores: list[str]
    fecha_salida: datetime

def leer_pelicula(atributos: list[str]) -> list[Pelicula]:
    fecha = atributos[4].split("/")
    fecha = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
    return Pelicula(
        atributos[0],
        int(atributos[1]), 
        int(atributos[2]), 
        atributos[3].split("-"),
        fecha
    )

# Forma 1. Sin readlines()
peliculas = []
with open("peliculas.csv", "r", encoding="utf-8") as f:
    contador_linea = 1
    for linea in f:
        if contador_linea > 1:
            atributos = linea.split(",")
            peliculas.append(leer_pelicula(atributos))
        contador_linea += 1

print("Las películas leaidas son: ")
[print(p) for p in peliculas]

# Forma 2. Con readlines()
peliculas = []
with open("peliculas.csv", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    peliculas = [leer_pelicula(linea.split(",")) for linea in lineas[1:]]

print("Las películas leidas son: ")
[print(p) for p in peliculas]