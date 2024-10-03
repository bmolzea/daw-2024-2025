Algoritmo ejercicio42
	
	Repetir
		num1 <- Azar(11)
		num2 <- Azar(11)
		operacion <- Azar(3)
		Segun operacion Hacer
			0:
				Escribir num1, " + ", num2
				Leer respuesta
				resultado <- num1+num2
			1:
				Escribir num1, " - ", num2
				Leer respuesta
				resultado <- num1-num2
				
			2:
				Escribir num1, " * ", num2
				Leer respuesta
				resultado <- num1*num2
		Fin Segun
		Si respuesta = resultado Entonces
			Escribir "Has acertado"
		SiNo
			Escribir "Has fallado"
		Fin Si
	Hasta Que respuesta = resultado

FinAlgoritmo
