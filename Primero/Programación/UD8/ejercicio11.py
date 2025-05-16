n_lineas = 0
n_palabras = 0
n_letras = 0

with open("quijote.txt", "r", encoding="utf-8") as f:
    for linea in f:
        n_lineas += 1
        n_letras += len(linea)
        n_palabras += len(linea.split())

with open("datos_quijote.txt", "w", encoding="utf-8") as f:
    f.write(f"El Quijote tiene {n_lineas} líneas {n_palabras} palabras y {n_letras} letras")