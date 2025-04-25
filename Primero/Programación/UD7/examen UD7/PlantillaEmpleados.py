from datetime import datetime
from Persona import Persona
from Empleado import Empleado

def dif_años(fecha1: datetime, fecha2: datetime) -> int:
    diferencia = fecha1.year - fecha2.year
    if (fecha1.month, fecha1.day) < (fecha2.month, fecha2.day):
        diferencia -= 1
    return diferencia

class PlantillaEmpleados:

    def __init__(self, empleados: list):
        self.empleados = empleados

    def __str__(self):
        resultado = ""
        for i, empleado in enumerate(self.empleados):
            resultado += f"[{i+1}] {empleado.nombre} - DNI: {empleado.dni}\n"
        return resultado
    
    def empleado_del_año(self, año: int):
        mejor_empleado = self.empleados[0]
        actual = len([premio for premio in mejor_empleado.empleado_del_mes if premio.year == año])
        for empleado in self.empleados:
            candidato = len([premio for premio in empleado.empleado_del_mes if premio.year == año])
            if candidato > actual or (candidato == actual and empleado.fecha_alta < mejor_empleado.fecha_alta):
                mejor_empleado = empleado
                actual = candidato
        return mejor_empleado

    def proponer_despidos(self) -> list:       
        propuestos = []
        hoy = datetime.now()
        for empleado in self.empleados:
            dif = dif_años(hoy, empleado.fecha_alta)
            if len(empleado.empleado_del_mes) / dif < 0.5:
                propuestos.append(empleado)
        return propuestos

    def despedir(self, dnis: list):
        for empleado in self.empleados:
            if empleado.dni in dnis:
                self.empleados.remove(empleado)
