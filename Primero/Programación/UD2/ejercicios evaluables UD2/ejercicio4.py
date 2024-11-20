def convertirPesos(cantidad: float, unidad1: str, unidad2:str) -> float:
    resultado = cantidad
    if unidad1 == "gr":
        if unidad2 == "kg":
            resultado /= 1000
        elif unidad2 == "t":
            resultado /= 1000000
    elif unidad1 == "kg":
        if unidad2 == "gr":
            resultado *= 1000
        elif unidad2 == "t":
            resultado /= 1000
    elif unidad1 == "t":
        if unidad2 == "gr":
            resultado *= 1000000
        elif unidad2 == "kg":
            resultado *= 1000
    
    return resultado

peso = float(input("Inserta el peso: "))
unidad1 = input("Inserta la unidad 1 (gr, kg, t): ")
unidad2 = input("Inserta la unidad 2 (gr, kg, t): ")
resultado = convertirPesos(peso, unidad1, unidad2)
print(f"{peso} {unidad1} son {resultado} {unidad2}")