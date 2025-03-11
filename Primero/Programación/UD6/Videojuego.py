class Videojuego:
   def __init__(self, nombre: str, generos: list, fecha_salida: str, puntuacion: float, PEGI: int, precio_base: float, peso: float):
       self.nombre = nombre
       self.generos = generos
       self.fecha_salida = fecha_salida
       self.puntuacion = puntuacion
       self.PEGI = PEGI
       self.precio_base = precio_base
       self.peso = peso # En GB


   def precio_final(self, impuestos: float, descuento: float) -> float:
       """
       Calcula el precio final aplicando impuestos y un descuento.
       :param impuestos: Porcentaje de impuestos a aplicar (ejemplo: 0.21 para 21%).
       :param descuento: Porcentaje de descuento a aplicar (ejemplo: 0.10 para 10%).
       :return: Precio final del videojuego.
       """
       precio_con_impuestos = self.precio_base * (1 + impuestos)
       precio_final = precio_con_impuestos * (1 - descuento)
       return round(precio_final, 2)
  
   def apto_menores(self) -> bool:
       """Devuelve True si el juego es apto para menores de edad (PEGI < 18), False en caso contrario."""
       return self.PEGI < 18
  
   def __str__(self):
       return (f"Nombre: {self.nombre}\n"
               f"Géneros: {', '.join(self.generos)}\n"
               f"Fecha de Salida: {self.fecha_salida}\n"
               f"Puntuación: {self.puntuacion}/10\n"
               f"PEGI: {self.PEGI}\n"
               f"Precio Base: {self.precio_base}€\n"
               f"Peso: {self.peso} GB\n"
               f"Apto para menores: {'Sí' if self.apto_menores() else 'No'}")