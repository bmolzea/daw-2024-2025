with open("quijote.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        if linea[0].lower() == "a":
            contador += 1

print(f"El Quijote tiene {contador} líneas que empiezan por a")

with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([linea for linea in lineas if linea[0].lower() == "a"])

print(f"El Quijote tiene {contador} líneas que empiezan por a")