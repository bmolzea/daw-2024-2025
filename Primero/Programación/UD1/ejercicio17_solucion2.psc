// Ejercicio resuelto con paréntesis
Algoritmo ejercicio17_solucion2
	// Esta variable solo puedo tener los valores de DAW, DAM, ASIR y SMR
	Escribir "Inserta tu ciclo:"
	Leer ciclo
	Escribir "Inserta tu curso:"
	Leer curso
	Si (ciclo="DAW" O ciclo="DAM") Y curso=1 Entonces
		Escribir "Cursas programación"
	SiNo
		Escribir "NO cursas programación"
	Fin Si
FinAlgoritmo