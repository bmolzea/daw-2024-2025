Algoritmo examen1_ejercio1
	Escribir "¿Cuántos dados quieres tirar?"
	Leer nTiradas
	Para i<-1 Hasta nTiradas Con Paso 1 Hacer
		resultado <- 1+Azar(6)
		Escribir "Tirada ",i,", resultado = ",resultado
	Fin Para
FinAlgoritmo
