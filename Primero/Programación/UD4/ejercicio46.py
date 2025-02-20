matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

suma = 0

# Forma correcta de hacerlo sin sum()
for fila in matriz:
    for n in fila:
        suma += n

print(suma)

suma = 0
# con sum
for fila in matriz:
    suma += sum(fila)

