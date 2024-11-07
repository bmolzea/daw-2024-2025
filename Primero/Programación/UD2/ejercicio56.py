def contarPalabras(frase: str) -> int:
    nPalabras = 1
    for caracter in frase:
        if caracter == " ":
            nPalabras = nPalabras + 1
    return nPalabras

frase = input("Inserta una frase: ")
nPalabras = contarPalabras(frase)
print(f"La frase tiene {nPalabras} palabras")