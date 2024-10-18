edad = int(input("Inserta tu edad:"))

if edad < 3:
    print("Eres un bebé")
elif edad >= 3 and edad <= 12:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 34:
    print("Adulto pero no")
elif edad == 35:
    print("La mejor edad")
elif edad >= 36 and edad <= 50:
    print("Adulto")
elif edad >= 51 and edad <= 67:
    print("Pre-anciano")
elif edad >= 68 and edad <= 99 :
    print("Eres anciano")
else:
    print("Eres centenario")