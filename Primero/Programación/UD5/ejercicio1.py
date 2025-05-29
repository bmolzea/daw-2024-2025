capitales = {
    'España':          'Madrid',
    'Canadá':          'Ottawa',
    'Australia':       'Canberra',
    'Japón':           'Tokio'
}

puntos = 0

for pais, capital in capitales.items():
    respuesta = input(f"¿Capital de {pais}? ")
    if respuesta.lower() == capital.lower():
        print(" Acertaste!!")
        puntos += 1
    else:
        print(f"Error! la capital es: {capital}")

total = len(capitales)
print(f"Has acertado {puntos} de {total} países")