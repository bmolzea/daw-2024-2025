dia = input("Inserta un día de la semana (L, M, X, J, V, S, D):")
habitacion = input("Selecciona tipo habitación (individual o doble):")
festivo = input("¿Es festivo? (si o no):")
cupon = input("¿Tienes cupón? (si o no):")
if cupon == "si":
    porcentajeCupon = float(input("Inserta el porcentaje del cupón: "))

if dia == "D" and festivo == "no":
    precio = 40 if habitacion == "individual" else 60
elif dia == "V" or dia == "S" or festivo == "si":
    precio = 45 if habitacion == "individual" else 70
else:
    precio = 30 if habitacion == "individual" else 50

if cupon == "si":
    descuento = precio * porcentajeCupon / 100
    precio -= descuento

print(f"El precio es: {round(precio, 2)}")