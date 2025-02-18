nombre = "Borja Molina Zea"
# Creo una lista con tres elementos: ["Borja", "Molina", "Zea"]
lista_nombre = nombre.split()
print(f"Mi primer apellido es {lista_nombre[1]}")

# Cadena que contiene los planetas separados por comas
planetas_txt = "Mercurio,Venus,La Tierra,Marte,Júpiter,Saturno,Urano,Neptuno"
planetas = planetas_txt.split(",")
print(f"El primer planeta es {planetas[0]} y el último es {planetas[-1]}")

# El antes
# paises = []
# while True:
#     pais = input("Inserta un país (fin para terminar): ")
#     if pais == "fin":
#         break
#     else:
#         paises.append(pais)
# print(paises)

# El ahora
paises_txt = input("Inserta países separados por comas: ")
paises = paises_txt.split(",")
print(paises)
