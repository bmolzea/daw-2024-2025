# Usando conjuntos (y si no nos importa el orden)
def sin_repetidos2(l: list) -> list:
    return list(set(l))

# Sin usar conjuntos
def sin_repetidos(l: list) -> list:
    resultado = []
    for element in l:
        if element not in resultado:
            resultado.append(element)
    return resultado

lista = [3, 4, 5, 4, 2, 1, 1, 0]
lista_sin_repetidos = sin_repetidos(lista.copy())
print(f"La lista {lista} sin números repetidos es: {lista_sin_repetidos}")