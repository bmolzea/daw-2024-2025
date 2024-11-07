import random

def operadorAleatorio()->str:
    codigo = random.randint(1, 3)
    if codigo == 1:
        operador = "+"
    elif codigo == 2:
        operador = "-"
    elif codigo == 3:
        operador = "*"
    
    return operador

def cuentaAleatoria(minimo: int, maximo: int) -> int:
    operando1 = random.randint(minimo, maximo)
    operando2 = random.randint(minimo, maximo)
    operador = operadorAleatorio()
    
    if operador == "+":
        resultado = operando1 + operando2
    elif operador == "-":
        resultado = operando1 - operando2
    elif operador == "*":
        resultado = operando1 * operando2
    
    print(f"{operando1} {operador} {operando2} = ?")

    return resultado

for i in range(10):
    resultado = cuentaAleatoria(1, 10)
    resultadoUsuario = int(input())
    if resultado == resultadoUsuario:
        print("Correcto!")
    else:
        print("Incorrecto")