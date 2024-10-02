Algoritmo ejercicio33
	Escribir "Inserta un número:"
	Leer num
	nDivisores <- 0
	Para i<-num Hasta 1 Con Paso -1 Hacer
		Si num MOD i = 0 Entonces
			nDivisores <- nDivisores + 1
		Fin Si
	Fin Para
	Si nDivisores = 2 Entonces
		Escribir num, " es primo"
	SiNo
		Escribir num, " NO es primo"
	Fin Si
FinAlgoritmo
