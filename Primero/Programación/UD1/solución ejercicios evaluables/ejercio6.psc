Algoritmo ejercicio6
	Escribir "Introduce un n�mero:"
	Leer num1
	Escribir "Introduce otro n�mero:"
	Leer num2
	Si num1>num2 Entonces
		grande <- num1
		peque <- num2
	SiNo
		grande <- num2
		peque <- num1
	Fin Si
	mcd <- 1
	Para i<-2 Hasta peque Con Paso 1 Hacer
		Si grande MOD i = 0 Y peque MOD i = 0 Entonces
			mcd <- i
		Fin Si
	Fin Para
	Escribir "El MCD es:",mcd
FinAlgoritmo
