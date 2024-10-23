dia = input("Inserta el día de la semana: (L, M, X, J, V, S, D)")
hora = int(input("Inserta la hora en la que coges el taxi: "))
kms = float(input("Inserta el número de kms: "))

if dia == "S": 
    if hora>=8 and hora <=18:
        tarifa = 1.2
    else:
        tarifa = 1.5
elif dia == "D":
    tarifa = 1.5
# El resto de días, es decir entre semana
else:
    if hora>=8 and hora<=18:
        tarifa = 1
    elif hora>=19 and hora<23:
        tarifa = 1.2
    elif hora == 23 or hora>=0 and hora<=7:
        tarifa = 1.5

coste = 3.5 + (tarifa * kms)
print(f"Supuesto que coges el taxi en {dia} a las {hora} horas y haces {kms} kilometros, el viaje te costaría {coste}")