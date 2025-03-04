planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]  # Incluyendo a Plutón
]

# Radio medio de los planetas gaseosos
gaseosos_radio = [planeta[2] for planeta in planetas if not planeta[1]]
gaseosos_radio_medio = sum(gaseosos_radio) / len(gaseosos_radio) 
print(f"El radio medio de los planetas gaseosos es: {gaseosos_radio_medio:.2f}")

# Radio medio de los planetas rocosos
rocosos_radio = [planeta[2] for planeta in planetas if planeta[1]]
rocosos_radio_medio = sum(rocosos_radio) / len(rocosos_radio) 
print(f"El radio medio de los planetas rocosos es: {rocosos_radio_medio:.2f}") 

# ¿Hay algún planeta rocoso más grande que uno gaseoso?
# Forma rápida (solo decimos si sí o si no)
hay = max(rocosos_radio) > min(gaseosos_radio)
if hay:
    print("Hay planetas rocosos más grandes que gaseosos")
else:
    print("No hay planetas rocosos más grandes que gaseosos")

# Sacando el nombre de los planetas
menor_radio_gaseoso = min(gaseosos_radio)
rocosos_grandes = [planeta[0] for planeta in planetas if planeta[1] and planeta[2] > menor_radio_gaseoso]
if len(rocosos_grandes):
    print(f"Hay planetas rocosos más grandes que gaseosos y estos son: {rocosos_grandes}")
else:
    print("No hay planetas rocosos más grandes que gaseosos")

# Nombre de los planetas que termina en no
terminan_no = [planeta[0] for planeta in planetas if planeta[0][-2:]=="no"]
print(f"Los planetas que termina en -no son: {terminan_no}")
