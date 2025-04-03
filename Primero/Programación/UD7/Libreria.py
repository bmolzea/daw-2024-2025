from EjemplarLibro import EjemplarLibro
class Libreria:
    
    def __init__(self, libros: list[EjemplarLibro]):
        self.libros = libros
        self.disponibles = []
        self.prestados = []

        for libro in self.libros:
            if libro.prestado:
                self.prestados.append(libro)
            else:
                self.disponibles.append(libro)
        

    def __str__(self)->str:
        libreria_str = "CATALOGO COMPLETO: \n"
        for libro in self.libros:
            libreria_str += f"{libro.titulo} - Estado: {libro.estado_str()} - ¿Disponible? {'Sí' if not libro.prestado else 'No'}\n"
        return libreria_str

    def n_ejemplares(self)->int:
        return len(self.libros)

    def n_libros(self)->int:
        return 0

    def quitar_libro(self, codigo_barras: str):
        pass

    def devolucion_atrasada(self)->list:
        pass

    def mandar_correo(self):
        pass

