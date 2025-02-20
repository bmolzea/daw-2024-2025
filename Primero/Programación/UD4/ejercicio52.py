alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

pos_peor_alumno = 0
nota_peor_alumno = sum(alumnos[0][1:])/3

for i, alumno in enumerate(alumnos):
    nueva_media = sum(alumnos[i][1:])/3
    if nueva_media < nota_peor_alumno:
        pos_peor_alumno = i

peor_alumno = alumnos[pos_peor_alumno][0]
print(f"El peor alumno es {peor_alumno} y su nota es {nota_peor_alumno}")