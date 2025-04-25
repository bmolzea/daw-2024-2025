from dataclasses import dataclass

# 1a)
@dataclass
class Pelicula:
    nombre: str
    duracion: int
    actores: list

# 1b)
peliculas = [
    Pelicula("El Padrino", 175, ["Marlon Brandon", "Al Pacino", "James Caan"]),
    Pelicula("Interstelar", 169, ["Mathew McConaughey", "Anne Hathawey", "Jessica Chastain"]),
    Pelicula("El Caballero oscuro", 152, ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Pelicula("Forrest Gump", 142, ["Tom Hanks", "Robin Wright", "Gary Sinese"]),
    Pelicula("Náufrago", 143, ["Tom Hanks", "Helen Hunt", "Nick Searcy"])
]

# 1c)
print("Todas las películas: ")
[print(pelicula) for pelicula in peliculas]

# 1d) 
print("\nPelículas que duran más de 150 mins y tienen actores con H")
for p in peliculas:
    if p.duracion > 150:
        for actor in p.actores:
            if actor[0] == "H":
                print(p.nombre)