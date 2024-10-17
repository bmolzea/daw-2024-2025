Algoritmo examen1_ejercicio4
	Escribir "Inserta el primer número:"
	Leer num1
	Escribir "Inserta el segundo número:"
	Leer num2
	Escribir "Inserta el tercer número:"
	Leer num3
	
	//Calculo el número mayor
	Si num1>num2 Y num1>num3 Entonces
		grande <- num1
	SiNo
		Si num2>num3 Entonces
			grande <- num2
		SiNo
			grande <- num3
		Fin Si
	Fin Si
	
	//Calculo el número menor
	Si num1<num2 Y num1<num3 Entonces
		peque <- num1
	SiNo
		Si num2<num3 Entonces
			peque <- num2
		SiNo
			peque <- num3
		Fin Si
	Fin Si
	
	Escribir "De los tres números que has introducido el más pequeño es ",peque," y el más grande es ",grande
FinAlgoritmo
