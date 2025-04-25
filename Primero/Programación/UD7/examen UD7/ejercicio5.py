from datetime import datetime
from Empleado import Empleado
from PlantillaEmpleados import PlantillaEmpleados

empleados = [
    Empleado("Laura Martínez", "12345678A", datetime(1987, 3, 12), False, False, 2800, datetime(2015, 6, 1), [datetime(2019, 2, 1), datetime(2020, 6, 1), datetime(2021, 9, 1), datetime(2022, 3, 1), datetime(2023, 11, 1), datetime(2022, 11, 1), datetime(2022, 7, 1), datetime(2024, 12, 1)]), 
    Empleado("Carlos Gómez", "12345679C", datetime(1990, 11, 8), False, False, 2500, datetime(2018, 9, 15), [datetime(2019, 5, 1), datetime(2020, 12, 23), datetime(2022, 7, 1), datetime(2023, 4, 1), datetime(2025, 1, 1), datetime(2020, 3, 1), datetime(2021, 8, 1), datetime(2023, 6, 3)]),
    Empleado("Ana Rodríguez", "12345645K", datetime(2020, 1, 20), False, False, 2700, datetime(2015, 6, 1), []),
    Empleado("Miguel Torres", "33345678L", datetime(1993, 4, 5), False, False, 2400, datetime(2019, 4, 10), [datetime(2020, 1, 1), datetime(2021, 10, 1), datetime(2023, 8, 1), datetime(2024, 2, 1)]),
    Empleado("Beatriz Navarro", "44345678A", datetime(2017, 11, 3), False, False, 3000, datetime(2015, 6, 1), [datetime(2022, 9, 1)])
]

plantilla = PlantillaEmpleados(empleados)

print(plantilla)

print("El mejor empleado del año 2023 es:")
print(plantilla.empleado_del_año(2023).nombre)

print("El mejor empleado del año 2019 es:")
print(plantilla.empleado_del_año(2019).nombre)

print("Propuestos para despido: ")
propuestos = plantilla.proponer_despidos()
[print(empleado.nombre) for empleado in propuestos]

print("Despedimos a los propuesto, la platilla queda como: ")
dnis = [propuesto.dni for propuesto in propuestos]
plantilla.despedir(dnis)
print(plantilla)