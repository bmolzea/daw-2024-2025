# Lista con los nombres de los planetas del sistema solar
planetas_sistema_solar = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]

# Lista con las masas de los planetas en kilogramos (valores aproximados)
masas_sistema_solar = [
   3.3011e23,  # Mercurio
   4.8675e24,  # Venus
   5.97237e24, # Tierra
   6.4171e23,  # Marte
   1.8982e27,  # Júpiter
   5.6834e26,  # Saturno
   8.6810e25,  # Urano
   1.02413e26  # Neptuno
]

masa_total = 0
for masa in masas_sistema_solar:
    masa_total += masa

masa_media = masa_total / len(masas_sistema_solar)
print(f"La masa media es {masa_media}")

# Saco los planetas cuya masa es superior a la media
print("Los planetas cuya masa es superior a la media son:")
for i, planeta in enumerate(planetas_sistema_solar):
    if masas_sistema_solar[i] > masa_media:
        print(planeta)

# Saco el planeta de mayor masa
mayor_masa = masas_sistema_solar[0]
i_mayor = 0
for i, masa in enumerate(masas_sistema_solar):
    if masa > mayor_masa:
        mayor_masa = masa
        i_mayor = i
planeta_gordo = planetas_sistema_solar[i_mayor]
print(f"El planeta más pesado es: {planeta_gordo}")