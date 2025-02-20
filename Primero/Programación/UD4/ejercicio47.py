matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

# sin .index()
fila_pos = 0
col_pos = 0

for i, fila in enumerate(matriz):
    for j, n in enumerate(fila):
        if n == 5:
            fila_pos = i
            col_pos = j
            break

print(f"5 está en la fila {fila_pos} y la columna {col_pos}")

# usando index
fila_pos = 0
col_pos = 0

for i, fila in enumerate(matriz):
    if fila.count(5)>0:
        fila_pos = i
        col_pos = fila.index(5)
        break

print(f"5 está en la fila {fila_pos} y la columna {col_pos}")