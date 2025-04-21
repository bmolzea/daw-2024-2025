# Sin readlines()
with open("quijote.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        palabras = linea.split()
        if len(palabras) > 0:
            if palabras[0].lower() == "don":
                contador += 1

print(f"{contador} líneas empiezan con Don (o don)")

# Con readliness()
with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([l for l in lineas if len(l.split())>0 and l.split()[0].lower() == "don"])

print(f"{contador} líneas empiezan con Don (o don)")