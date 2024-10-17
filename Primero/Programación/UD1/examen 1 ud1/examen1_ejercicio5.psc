Algoritmo examen1_ejercicio5
	peque <- 0
	grande <- 0
	Repetir
		Escribir "Inserta un número (cero para terminar):"
		Leer num
		Si num>grande Entonces
			grande <- num
		Fin Si
		Si num<peque Entonces
			peque <- num
		Fin Si
	Hasta Que num = 0
	Escribir "De todos los números que has introducido..."
	Escribir grande," es el mayor"
	Escribir peque," es el menor"
FinAlgoritmo
