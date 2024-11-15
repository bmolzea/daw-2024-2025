def contarVocales(palabra: str) -> int:
    nVocales = 0
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            nVocales = nVocales + 1
    return nVocales

palabra = input("Inserta una palabra: ")
nVocales = contarVocales(palabra)
print(f"La palabra {palabra} tiene {nVocales} vocales")