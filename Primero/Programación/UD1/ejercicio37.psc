Algoritmo ejercicio37
	Repetir
		Escribir "¿Qué quieres calcular?"
		Escribir "1. Seno"
		Escribir "2. Coseno"
		Escribir "3. Tangente"
		Escribir "4. ArcoSeno"
		Escribir "5. ArcoCoseno"
		Escribir "6. ArcoTangente"
		Escribir "0. Salir"
		Leer seleccion
		Si seleccion <> 0 Entonces
			Escribir "Introduce un ángulo:"
			Leer angulo
		Fin Si
		
		Segun seleccion Hacer
			1:
				Escribir "El seno de ", angulo, " es:",sen(angulo)
			2:
				Escribir "El coseno de ", angulo, " es:",cos(angulo)
			3:
				Escribir "La tangente de ", angulo, " es:",tan(angulo)
			4:
				Escribir "El arcoseno de ", angulo, " es:",asen(angulo)
			5:
				Escribir "El arcocoseno de ", angulo, " es:",acos(angulo)
			6:
				Escribir "La arcotangente de ", angulo, " es:",atan(angulo)
		Fin Segun
	Hasta Que seleccion = 0
FinAlgoritmo
