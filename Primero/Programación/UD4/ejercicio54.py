alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

suma = 0
n_alumnos = len(alumnos)

for alumno in alumnos:
    suma += sum(alumno[1:])/3

nota_media = suma / n_alumnos
print(f"La nota media de la clase es: {nota_media}")
