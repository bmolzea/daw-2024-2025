def es_cuadrada(matriz: list) -> bool:
    return len(matriz) == len(matriz[0])

def es_cuadrada2(matriz: list) -> bool:
    cuadrada = True
    n_filas = len(matriz)
    for fila in matriz:
        if len(fila) != n_filas:
            cuadrada = False
            break
    return cuadrada


m = [
    [1, 2],
    [3, 4]
]

m2 = [
    [1, 2, 3],
    [3, 5, 6]
]

print(es_cuadrada2(m))
print(es_cuadrada2(m2))