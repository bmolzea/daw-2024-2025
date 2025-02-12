precipitaciones_granada_2023 = [
   40.2,  # Enero
   35.6,  # Febrero
   45.8,  # Marzo
   50.1,  # Abril
   30.3,  # Mayo
   10.4,  # Junio
   1.2,   # Julio
   5.6,   # Agosto
   20.8,  # Septiembre
   60.5,  # Octubre
   55.3,  # Noviembre
   42.7   # Diciembre
]

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Opción profe
for i, prec in enumerate(precipitaciones_granada_2023):
    if i<11 and precipitaciones_granada_2023[i+1] > prec:
        print(f"En {meses[i+1]} llovió más que {meses[i]}")

print("--------------------------")

# Opción Fran
for i in range(1, len(precipitaciones_granada_2023)):
    prec_actual =  precipitaciones_granada_2023[i]
    prec_anterior =  precipitaciones_granada_2023[i-1]
    if prec_actual > prec_anterior:
        print(f"En el mes {meses[i]} llovió más que en {meses[i-1]}")