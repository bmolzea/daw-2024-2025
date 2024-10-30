texto = input("Introduce un texto: ")
letra = input("Introduce la letra: ")
nLetras = 0
for caracter in texto:
    if letra == caracter:
        nLetras = nLetras + 1
print(f"El texto {texto} tienes {nLetras} {letra}")