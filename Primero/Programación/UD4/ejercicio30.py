# Lista con los nombres de los planetas del sistema solar
planetas = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]

# Lista con las masas de los planetas en kilogramos (valores aproximados)
masas_planetas = [
   3.3011e23,  # Mercurio
   4.8675e24,  # Venus
   5.97237e24, # Tierra
   6.4171e23,  # Marte
   1.8982e27,  # Júpiter
   5.6834e26,  # Saturno
   8.6810e25,  # Urano
   1.02413e26  # Neptuno
]

radios_planetas = [
    2439.7,  # Mercurio
    6051.8,  # Venus
    6371.0,  # Tierra
    3389.5,  # Marte
    69911.0, # Júpiter
    58232.0, # Saturno
    25362.0, # Urano
    24622.0  # Neptuno
]

while True:
    planeta = input("Dime un planeta: ")
    if planetas.count(planeta) > 0:
        i = planetas.index(planeta)
        print(f"{planeta} pesa {masas_planetas[i]} y su radio es {radios_planetas[i]}")
    else:
        print("El planeta no existe")