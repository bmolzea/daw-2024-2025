Algoritmo ejercicio38
	Escribir  "Introduce un número:"
	Leer tam
	Repetir
		Escribir  "Introduce una palabra:"
		Leer palabra
		Si tam <> Longitud(palabra) Entonces
			Escribir "He dicho que de ", tam, " letras!!!!!"
		Fin Si
	Hasta Que tam = Longitud(palabra)
	
	
FinAlgoritmo
