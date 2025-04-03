class Libro:
  
   def __init__(self, titulo: str, autores: list, generos: list, n_palabras: int):
       self.titulo = titulo
       self.autores = autores
       self.generos = generos


       if n_palabras >= 0:
           self.n_palabras = n_palabras
       else:
           self.n_palabras = 0
  
   def __str__(self):
       return (
           f"Título: {self.titulo}\n"
           f"Autores: {self.autores}, "
           f"Géneros: {self.generos}, "
           f"Número de palabras: {self.n_palabras}"
       )

   def __eq__(self, other) -> bool:
       if isinstance(other, Libro):
           return self.titulo == other.titulo and self.autores == other.autores
       return False


   def __lt__(self, other) -> bool:
        return self.n_palabras < other.n_palabras

   def __le__(self, other) -> bool:
       return self.n_palabras <= other.n_palabras


   def __gt__(self, other) -> bool:
       return self.n_palabras > other.n_palabras

   def __ge__(self, other) -> bool:
       return self.n_palabras >= other.n_palabras


   def __len__(self) -> int:
       return self.n_palabras


   def __contains__(self, palabra: str) -> bool:
       return palabra in self.titulo.split()


   def longitud(self) -> str:
       longitudes = ["Corto", "Mediano", "Largo"]
       if self.n_palabras < 10000:
           longitud = longitudes[0]
       elif self.n_palabras >= 10000 and self.n_palabras <= 40000:
           longitud = longitudes[1]
       else:
           longitud = longitudes[2]
       return longitud


