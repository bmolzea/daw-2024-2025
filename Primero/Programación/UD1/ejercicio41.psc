Algoritmo ejercicio41
	Escribir  "Inserta el número mínimo:"
	Leer minimo
	Escribir "Inserta el número máximo:"
	Leer maximo
	Escribir "¿Cuántos números aleatorios entre ",minimo," y ",maximo," quieres crear?"
	Leer nVeces
	Para i<-1 Hasta nVeces Con Paso 1 Hacer
		Escribir minimo+Azar(maximo-minimo+1)
	Fin Para
FinAlgoritmo
