diccionario = {
    'Lista': 'Colección ordenada de elementos, accesibles por índices.',
    'Conjunto': 'Colección de elementos únicos sin orden predefinido.',
    'Diccionario': 'Estructura de datos que almacena pares clave–valor, permitiendo acceder rápidamente a los datos asociados a cada clave.'
}

while True:
    palabra = input("Introduce una palabra: ")
    
    if palabra == 'salir':
        print("Chao pescao")
        break
    
    definicion = diccionario.get(palabra)
    
    if definicion != None:
        print(f"{palabra}: {definicion}\n")
    else:
        print("La palabra no está en el diccionario")



