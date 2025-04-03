from EdicionLibro import EdicionLibro
from datetime import datetime

class EjemplarLibro(EdicionLibro):
    
    def __init__(self, ISBN: str, titulo: str, autores: list, generos: list, n_palabras: int, precio_base: float, tipo_edicion: str, editorial: str, n_paginas: int, dimensiones: list, codigo_barras: str, estado: int, n_veces_prestado: int, prestado: bool, fecha_inicio_prestamo: datetime = None, fecha_fin_prestamo: datetime = None, dni_prestamo_actual: str = ""):

        super().__init__(ISBN, titulo, autores, generos, n_palabras, precio_base, tipo_edicion, editorial, n_paginas, dimensiones)

        self.codigo_barras = codigo_barras
        self.estado = estado
        self.n_veces_prestado = n_veces_prestado
        self.prestado = prestado
        self.fecha_inicio_prestamo = fecha_inicio_prestamo
        self.fecha_fin_prestamo = fecha_fin_prestamo
        self.dni_prestamo_actual = dni_prestamo_actual

    def estado_str(self) -> str:
        estado = "Desconocido"
        
        if self.estado == 1:
            estado = "Nuevo"
        elif self.estado == 2:
            estado = "Como nuevo"
        elif self.estado == 3:
            estado = "Desgastado"
        elif self.estado == 4: 
            estado = "Desperfectos menores"
        elif self.estado == 5:
            estado = "Desperfectos mayores"

        return estado

    def __str__(self)->str:
        return super().__str__() + (
           f", estado: {self.estado_str()}\n"
           f"¿Disponible?: {'Sí' if not self.prestado else f'No'} "
        )  
    
    def __eq__(self, other)->bool:
        return self.codigo_barras == other.codigo_barras
        


    
