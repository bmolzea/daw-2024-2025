peso = float(input("Inserta el peso de tu coche: (en tonelada)"))

if peso < 1:
    print("Es un coche ligero")
elif peso >= 1 and peso <= 2:
    print("Es un coche mediano")
else:
    print("Es un coche pesado")