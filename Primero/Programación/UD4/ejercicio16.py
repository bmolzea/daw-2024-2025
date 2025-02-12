"""
Crea un programa con una lista que contenga el resultado de haber lanzado 10 veces una moneda al aire (cara o cruz). 
"""

import random

def lanzar_moneda()->str:
    n = random.randint(0, 1)
    if n == 0:
        return "Cara"
    else:
        return "Cruz"
    
lanzamientos = []
for _ in range(10):
    lanzamientos.append(lanzar_moneda())

print(lanzamientos)