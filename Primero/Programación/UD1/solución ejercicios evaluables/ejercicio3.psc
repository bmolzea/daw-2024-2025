Algoritmo ejercicio3
	Escribir "¿Cuántas veces quieres lanzar la moneda?"
	Leer nVeces
	Para i<-1 Hasta nVeces Con Paso 1 Hacer
		tirada <- Azar(2)
		Si tirada = 1 Entonces
			Escribir "Cara"
		SiNo
			Escribir "Cruz"
		Fin Si
	Fin Para
FinAlgoritmo
