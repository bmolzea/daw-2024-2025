Algoritmo ejercicio41
	Escribir  "Inserta el n�mero m�nimo:"
	Leer minimo
	Escribir "Inserta el n�mero m�ximo:"
	Leer maximo
	Escribir "�Cu�ntos n�meros aleatorios entre ",minimo," y ",maximo," quieres crear?"
	Leer nVeces
	Para i<-1 Hasta nVeces Con Paso 1 Hacer
		Escribir minimo+Azar(maximo-minimo+1)
	Fin Para
FinAlgoritmo
