Algoritmo ejercicio2
	Repetir
		Escribir "�Qu� quieres calcular?"
		Escribir "1. �rea tri�ngulo"
		Escribir "2. �rea rect�ngulo"
		Escribir "3. �rea circunferencia"
		Escribir "0. Salir"
		Leer seleccion
		Segun seleccion Hacer
			1:
				Escribir "Introduce la base:"
				Leer base
				Escribir "Introduce la altura:"
				Leer altura
				area <- base * altura / 2
				Escribir "El �rea es: ",area
			2:
				Escribir "Introduce la base:"
				Leer base
				Escribir "Introduce la altura:"
				Leer altura
				area <- base * altura
				Escribir "El �rea es: ",area
			3:
				Escribir "Introduce el radio:"
				Leer radio
				area <- PI*radio*radio
				Escribir "El �rea es: ",area
		Fin Segun
	Hasta Que seleccion = 0
FinAlgoritmo
