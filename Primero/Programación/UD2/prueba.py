def imc(peso: float, altura: float) -> str:
    imc = peso/(altura*altura)
    if imc < 18.5:
        resultado = "Peso bajo"
    elif imc >= 18.5 and imc< 24.9:
        resultado = "Peso óptimo"
    elif imc >= 24.9 and imc < 30:
        resultado = "Sobrepeso"
    else:
        resultado = "Obesidad"
   
    return resultado

p = float(input("Inserta tu peso: "))
a = float(input("Inserta tu altura: "))

print(imc(p, a))