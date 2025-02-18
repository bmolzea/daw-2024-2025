liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club","Villarreal CF","Rayo Vallecano","Girona FC","CA Osasuna","RCD Mallorca","Real Betis Balompié","Real Sociedad","Celta de Vigo","Sevilla FC","Getafe CF","UD Las Palmas","RCD Espanyol","CD Leganés","Valencia CF","Deportivo Alavés","Real Valladolid"]


# Seleccionamos los tres primeros equipos
print(liga[0:3])
# También podemos hacer
print(liga[:3])


# Seleccionamos los equipos entre la posición 5 y 10
print(liga[4:10])


# Seleccionamos los 4 últimos equipos
print(liga[-4:])


# Mostramos los equipos clasificados de la mitad hacía arriba
mitad = len(liga) // 2
print(liga[:mitad])
# Mostramos los equipos clasificados de la mitad hacia abajo
print(liga[mitad:])

