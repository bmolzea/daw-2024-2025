"""
Ejercicio 6.
-Crea la dataclass Planeta, con los siguientes atributos: nombre (str), rocoso (bool) y num_lunas(int).
-Crea una lista con los siguientes 9 objetos de la clase:
-Muestra por pantalla todos los objetos de la lista mostrando todos sus atributos
-Filtra la lista para que contenga los planetas rocosos sin lunas. Muestra por pantalla su nombre.
"""
from dataclasses import dataclass

# a) Crea la dataclass Planeta, con los siguientes atributos: nombre (str), rocoso (bool) y num_lunas(int). 
@dataclass
class Planeta:
    nombre: str
    rocoso: bool
    num_lunas: int

# b) Crea una lista con los siguientes 9 objetos de la clase:
planetas = [
    Planeta("Mercurio", True, 0),
    Planeta("Venus", True, 0),
    Planeta("Tierra", True, 1),
    Planeta("Marte", True, 2),
    Planeta("Jupiter", False, 95),
    Planeta("Saturno", False, 146),
    Planeta("Urano", False, 27),
    Planeta("Neptuno", False, 14),
    Planeta("Pluton", True, 5),
]

# c) Muestra por pantalla todos los objetos de la lista mostrando todos sus atributos
for planeta in planetas:
    print(planeta)

# c) con list comprehension
# [print(planeta) for planeta in planetas]


# d) Filtra la lista para que contenga los planetas rocosos sin lunas. Muestra por pantalla su nombre. 

# Método 1
rocosos = []
print("\nPlanetas rocosos sin lunas: ")
for p in planetas:
    if p.rocoso and p.num_lunas == 0:
        rocosos.append(p)
        print(p)

# Método 2
print("\nPlanetas rocosos sin lunas: ")
rocosos = [p for p in planetas if p.rocoso and p.num_lunas == 0]
for p in rocosos:
    print(p)

# Método 3
print([p for p in planetas if p.rocoso and p.num_lunas == 0])

# Método 4
[print(p) for p in planetas if p.rocoso and p.num_lunas == 0]