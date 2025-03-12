from datetime import datetime
import math


class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, descubierto: datetime, lunas: list):
        """
        Clase que representa un planeta.

        :param nombre: Nombre del planeta.
        :param masa: Masa del planeta en kilogramos.
        :param radio: Radio del planeta en metros.
        :param descubierto: Fecha de descubrimiento (datetime).
        :param lunas: Lista de lunas, cada una representada por [nombre, radio, masa].
        """
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.descubierto = descubierto
        self.lunas = lunas

    def get_densidad(self) -> float:
        """
        Calcula la densidad del planeta en kg/m³.
        Fórmula: densidad = masa / volumen
        Volumen de una esfera: (4/3) * π * r³
        """
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen if volumen > 0 else 0

    def __str__(self):
        """
        Representación en cadena del planeta.
        """
        fecha_desc = self.descubierto.strftime("%Y-%m-%d")  # Convertir datetime a string
        lunas_info = ", ".join([f"{luna[0]} (radio: {luna[1]}m, masa: {luna[2]}kg)" for luna in self.lunas])
        return (f"🌍 Planeta: {self.nombre}\n"
                f"   - Masa: {self.masa} kg\n"
                f"   - Radio: {self.radio} m\n"
                f"   - Descubierto: {fecha_desc}\n"
                f"   - Densidad: {self.get_densidad():.2f} kg/m³\n"
                f"   - Lunas: {lunas_info if lunas_info else 'No tiene'}")
