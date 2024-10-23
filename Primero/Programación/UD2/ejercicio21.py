#tipoVia = {Autovía, Nacional}
tipoVia = "Nacional"
#tipoVehiculo = {"Coche", "Bus", "Camión"}
tipoVehiculo = "Bus"

velocidadMax = -1

if tipoVia == "Autovía":
    if tipoVehiculo == "Coche":
        velocidadMax = 120
    elif tipoVehiculo == "Bus":
        velocidadMax = 110
    elif tipoVehiculo == "Camión":
        velocidadMax = 100
elif tipoVia == "Nacional":
    if tipoVehiculo == "Coche" or tipoVehiculo == "Bus":
        velocidadMax = 100
    elif tipoVehiculo == "Camión":
        velocidadMax = 90

print(f"El tipo de vehiculo {tipoVehiculo} por el tipo de vía {tipoVia} puede ir como máximo a {velocidadMax}")