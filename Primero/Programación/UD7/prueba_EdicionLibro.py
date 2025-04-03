from EdicionLibro import EdicionLibro

libros = [
    EdicionLibro("234-987", "El Quijote", ["Cervantes"], ["historia", "comedia"], 234534, 5, "Tapa blanda", "brr brr patapim", 700, [7, 13]),
    EdicionLibro("123-321", "El Quijote", ["Cervantes"], ["historia", "comedia"], 234534, 10, "Tapa dura", "brr brr patapim", 599, [11, 15]),
    EdicionLibro("192-456", "Hamlet", ["Shakespeare"], ["drama", "misterio"], 98000, 10, "Tapa dura", "brr brr patapim", 128, [11, 15]),
    EdicionLibro("185-234", "Hamlet", ["Shakespeare"], ["drama", "misterio"], 98000, 5, "Tapa blanda", "brr brr patapim", 100, [11, 15])
]

# Aplicamos descuento del 50% a los libros cuyo género sea "historia"
# for libro in libros:
#     if "historia" in libro.generos:
#         libro.aplicar_descuento(0.50)

# Aplicamos el descuento utilizando list comprehension

[libro.aplicar_descuento(0.5) for libro in libros if "historia" in libro.generos]
        
for libro in libros:
    print(libro)
        
