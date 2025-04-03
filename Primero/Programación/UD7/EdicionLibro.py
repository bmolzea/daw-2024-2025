from Libro import Libro


class EdicionLibro(Libro):
   def __init__(self, ISBN: str, titulo: str, autores: list, generos: list, n_palabras: int, precio_base: float, tipo_edicion: str, editorial: str, n_paginas: int, dimensiones: list):
       super().__init__ (titulo, autores, generos, n_palabras)

       self.ISBN = ISBN

       if precio_base >= 0:
           self.precio_base = round(precio_base, 2)
       else:
           self.precio_base = 0
       self.precio_venta = self.precio_base

       self.tipo_edicion = tipo_edicion
       self.editorial = editorial
       self.n_paginas = n_paginas
       # El primer número es el ancho y el segundo el alto
       self.dimensiones = dimensiones 


   def aplicar_descuento(self, descuento: float):
       self.precio_venta = round(self.precio_base - self.precio_base * descuento, 2)


   def tamaño(self)->str:
       tamaños = ["Pequeño", "Mediano", "Grande"]
       if self.dimensiones[1] <= 8:
           tam = tamaños[0]
       elif self.dimensiones[1] > 8 and self.dimensiones[1] <= 12:
           tam  = tamaños[1]
       else:
           tam = tamaños[2]
           
       return tam


   def __str__(self):
       return super().__str__() + (
           f", ISBN: {self.ISBN}, "
           f"Precio: {self.precio_venta}, "
           f"Tipo edición: {self.tipo_edicion}, "
           f"Editorial: {self.editorial}, "
           f"Precio de venta: {self.precio_venta}€"
       )

