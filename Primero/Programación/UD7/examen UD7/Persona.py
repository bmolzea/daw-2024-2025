from datetime import datetime

class Persona:

    def __init__(self, nombre: str, dni: str, fecha_nacimiento: datetime, casado: bool, divorciado: bool): 
        
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento if fecha_nacimiento < datetime.now() else None
        self.casado = casado
        self.divorciado = divorciado

        if self.casado and self.divorciado:
            self.casado = False
            self.divorciado = False

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.dni == other.dni
        else:
            return False
        
    def edad(self) -> int:
        hoy = datetime.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad
    
    def estado_civil(self) -> str:
        if self.casado:
            return "casado"
        elif self.divorciado:
            return "divorciado"
        else:
            return "soltero"
        
    def __str__(self) -> str:
        return f"{self.nombre}\n DNI: {self.dni}, fecha nacimiento: {self.fecha_nacimiento.strftime('%d/%m/%y')}, edad: {self.edad()}, estado civil: {self.estado_civil()}"