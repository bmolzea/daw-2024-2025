Algoritmo examen1_ejercicio4
	Escribir "Inserta el primer n�mero:"
	Leer num1
	Escribir "Inserta el segundo n�mero:"
	Leer num2
	Escribir "Inserta el tercer n�mero:"
	Leer num3
	
	//Calculo el n�mero mayor
	Si num1>num2 Y num1>num3 Entonces
		grande <- num1
	SiNo
		Si num2>num3 Entonces
			grande <- num2
		SiNo
			grande <- num3
		Fin Si
	Fin Si
	
	//Calculo el n�mero menor
	Si num1<num2 Y num1<num3 Entonces
		peque <- num1
	SiNo
		Si num2<num3 Entonces
			peque <- num2
		SiNo
			peque <- num3
		Fin Si
	Fin Si
	
	Escribir "De los tres n�meros que has introducido el m�s peque�o es ",peque," y el m�s grande es ",grande
FinAlgoritmo
