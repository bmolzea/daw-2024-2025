def imprime_matriz(matriz: list):
    for fila in matriz:
        for n in fila:
            print(n, end=" ")
        print()

matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for fila in matriz:
    for j, n in enumerate(fila):
        if n < 0:
            fila[j] = fila[j] * -1


imprime_matriz(matriz)