from random import randint
 
def nota_aleatoria() -> str:
    notas = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    n_notas = len(notas)
    return notas[randint(0, n_notas-1)]

def nota_aleatoria_sin(excluida: str) -> str:
    notas = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    notas.remove(excluida)
    n_notas = len(notas)
    return notas[randint(0, n_notas-1)]

def todos_iguales(l: list) -> bool:
    tam = len(l)
    if tam > 0:
       iguales = l.count(l[0]) == tam
    else:
        iguales = False
    return iguales

def generar_partitura(longitud: int, n_repeticiones: int) -> list:
    partitura = []
    for _ in range(longitud):
        if not todos_iguales(partitura[-n_repeticiones:]):
            partitura.append(nota_aleatoria())
        else: 
            partitura.append(nota_aleatoria_sin(partitura[-1]))
    return partitura


print(generar_partitura(20, 2))
