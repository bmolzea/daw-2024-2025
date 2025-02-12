"""
Escribe un programa que genere una lista con los pares comprendidos entre a y b. Los parámetros a y b son leídos desde el teclado. (Hacerlo sin listas y con listas)
"""
while True:
    a = int(input("Inserta el número inicial: "))
    b = int(input("Inserta el número final: "))
    if a <= b :
        break
    else:
        print("El número final no puede ser menor al inicial")


pares = []

for n in range(a, b+1):
    if n % 2 == 0:
        pares.append(n)     