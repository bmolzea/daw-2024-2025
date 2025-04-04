from datetime import datetime

# Dadas dos fechas devulve la diferencia en día
def dif_dias(fecha1: datetime, fecha2: datetime) -> int:
    return (fecha1-fecha2).days