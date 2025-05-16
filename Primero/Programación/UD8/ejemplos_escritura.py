nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")

with open("datos_ejemplo_escritura.txt", "a", encoding="utf-8") as f:
    f.write(f"Te llamas: {nombre} y tienes {edad} años")