from EjemplarLibro import EjemplarLibro
from Libro import Libro
from utils import dif_dias
from datetime import datetime

class Biblioteca:
    
    def __init__(self, libros: list[EjemplarLibro]):
        self.libros = libros
        

    def __str__(self)->str:
        libreria_str = "CATALOGO COMPLETO: \n"
        for libro in self.libros:
            libreria_str += f"{libro.titulo} - Estado: {libro.estado_str()} - ¿Disponible? {'Sí' if not libro.prestado else 'No'}\n"
        return libreria_str

    def obtener_disponibles(self)->list:
        return [libro for libro in self.libros if not libro.prestado]

    def mostrar_disponibles(self)->str:
        print("Libros disponibles para préstamo: ")
        for libro in self.obtener_disponibles():
            print(f"{libro.titulo}, estado: {libro.estado_str()}")
    
    def obtener_prestados(self)->list:
        return [libro for libro in self.libros if libro.prestado]

    def mostrar_prestados(self)->str:
        print("Libros prestados: ")
        for libro in self.obtener_prestados():
            if libro.prestado:
                print(f"{libro.titulo}, prestado a: {libro.dni_prestamo_actual}, fecha devolución: {libro.fecha_fin_prestamo.strftime('%d/%m/%y')}")

    # Lista de libros distintos que tiene la biblioteca
    # Es decir si hay múltiples ejemplares del Quijote solo mostramos uno
    def obtener_libros_distintos(self)->list:
        distintos = []
        for ejemplar in self.libros:
            libro = Libro(ejemplar.titulo, ejemplar.autores, ejemplar.generos, ejemplar.n_paginas)
            if libro not in distintos:
                distintos.append(libro)
        return distintos
   
    def mostrar_libros_distintos(self):
        distintos = self.obtener_libros_distintos()
        for libro in distintos:
            print(f"{libro.titulo} -- {libro.autores[0]}")
    
    # Quitamos un ejemplar de la biblioteca especificando su código de barras
    # Método útil si un ejemplar se pierde o lo roban
    def quitar_libro(self, codigo_barras: str):
        for libro in self.libros:
            if libro.codigo_barras == codigo_barras:
                self.libros.remove(libro) 

    # Devolvemos una lista con los libros que deberían haber sido devueltos y aún no lo están
    def devolucion_atrasada(self)->list:
        atrasados = []
        for libro in self.libros:
            if libro.prestado:
                dif = dif_dias(libro.fecha_fin_prestamo, datetime.now())
                if dif < 0:
                    atrasados.append([libro, dif])
        return atrasados


    def mostrar_devoluciones_atrasadas(self):
        print("Los libros que deberían haber sido devueltos son: ")
        for atraso in self.devolucion_atrasada():
            libro = atraso[0]
            dias_retraso = atraso[1]
            print(f"{libro.codigo_barras} lo tiene {libro.dni_prestamo_actual} y lleva un restraso de {-dias_retraso} días")




