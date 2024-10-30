texto = "En un lugar de la Mancha de cuyo nombre no me quiero acordar"
nEspacios = 0

for caracter in texto:
    if caracter == " ":
        nEspacios = nEspacios + 1

nPalabras = nEspacios + 1
print(f"La frase tiene {nPalabras} palabras")