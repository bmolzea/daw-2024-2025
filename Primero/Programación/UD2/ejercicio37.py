num = int(input("Introduce un número: "))
resultado = 1
for i in range(2, num + 1):
    resultado = resultado * i

print(f"El factorial {num} es {resultado}")