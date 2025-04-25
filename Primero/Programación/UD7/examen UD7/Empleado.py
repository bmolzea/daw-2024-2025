from datetime import datetime
from Persona import Persona

class Empleado(Persona):

    def __init__(self, nombre: str, dni: str, fecha_nacimiento: datetime, casado: bool, divorciado: bool, sueldo: float, fecha_alta: datetime, empleado_del_mes: list):
        super().__init__(nombre, dni, fecha_nacimiento, casado, divorciado)
        self.sueldo = sueldo
        self.fecha_alta = fecha_alta
        self.empleado_del_mes = empleado_del_mes

    def __gt__(self, other):
        return self.sueldo > other.sueldo

    def __ge__(self, other):
        return self.sueldo >= other.sueldo

    def __lt__(self, other):
        return self.sueldo < other.sueldo

    def __le__(self, other):
        return self.sueldo <= other.sueldo

    def n_veces_empleado_mes(self) -> int:
        return len(self.empleado_del_mes)

    def ultima_vez_empleado_mes(self) -> datetime:
        if not self.empleado_del_mes:
            return None
        return max(self.empleado_del_mes)
    
    def __str__(self) -> str:
        resultado = super().__str__() + f"\n Sueldo: {self.sueldo}, fecha alta: {self.fecha_alta.strftime('%d/%m/%y')}, número de veces empleado del mes: {self.n_veces_empleado_mes()}"
        if self.n_veces_empleado_mes() > 0:
            resultado += f", última vez: {self.ultima_vez_empleado_mes().strftime('%m/%y')}"        
        return resultado


    