calificacion = int(input("Inserta tu calificación:"))

if calificacion <= 100 and calificacion >= 90:
    print("A")
elif calificacion <= 89 and calificacion >= 80:
    print("B")
elif calificacion <= 79 and calificacion >= 70:
    print("C")
elif calificacion <= 69 and calificacion >= 60:
    print("D")
else:
    print("F")