def tablaMultiplicar(num: int):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

for i in range(1, 11):
    print(f"Tabla del {i} :")
    tablaMultiplicar(i)
