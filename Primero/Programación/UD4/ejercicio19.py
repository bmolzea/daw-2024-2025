"""
 Crea una lista llamada nombres con los valores ["Ana", "Carlos", "Lucía"]. Usa insert() para agregar "Beatriz" entre "Ana" y "Carlos". Usa insert() para agregar "Diego" al final de la lista. Imprime la lista después de cada operación.
"""

nombres = ["Ana", "Carlos", "Lucía"]
nombres.insert(1, "Beatriz")
nombres.insert(len(nombres), "Diego")
print(nombres)