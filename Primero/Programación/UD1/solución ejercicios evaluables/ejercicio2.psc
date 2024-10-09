Algoritmo ejercicio2
	Repetir
		Escribir "¿Qué quieres calcular?"
		Escribir "1. Área triángulo"
		Escribir "2. Área rectángulo"
		Escribir "3. Área circunferencia"
		Escribir "0. Salir"
		Leer seleccion
		Segun seleccion Hacer
			1:
				Escribir "Introduce la base:"
				Leer base
				Escribir "Introduce la altura:"
				Leer altura
				area <- base * altura / 2
				Escribir "El área es: ",area
			2:
				Escribir "Introduce la base:"
				Leer base
				Escribir "Introduce la altura:"
				Leer altura
				area <- base * altura
				Escribir "El área es: ",area
			3:
				Escribir "Introduce el radio:"
				Leer radio
				area <- PI*radio*radio
				Escribir "El área es: ",area
		Fin Segun
	Hasta Que seleccion = 0
FinAlgoritmo
