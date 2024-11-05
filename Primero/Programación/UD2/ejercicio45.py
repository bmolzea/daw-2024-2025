while True:
    precioBase = float(input("Inserta un precio base: "))
    if precioBase < 0:
        break
    ivaPorcentaje = float(input("Inserta un iva: "))
    sobrecoste = precioBase * ivaPorcentaje / 100
    precioFinal = round(precioBase + sobrecoste, 2)
    print(f"El precio final es: {precioFinal}")