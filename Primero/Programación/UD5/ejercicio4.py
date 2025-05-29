traductor = {
    'hello':     'hola',
    'goodbye':   'adiós',
    'thank you': 'gracias',
    'please':    'por favor',
    'yes':       'sí',
    'no':        'no'
}


while True:
    palabra = input("Palabra en inglés? ")
    if palabra == 'salir':
        print("Chao pescao")
        break

    if palabra in traductor:
        print(f"Traducción: {traductor[palabra]}\n")
    else:
        print("La palabra no está en el diccionario ")
        traduccion = input("Traducción en español? ")
        traductor[palabra] = traduccion
