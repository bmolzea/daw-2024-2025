def factorial(n: int) -> int:
    resultado = 1
    for i in range(2, n+1):
        resultado = resultado * i
    return resultado

n = int(input("Inserta un número: "))
resultado = factorial(n)
print(f"El factorial de {n} es {resultado}")