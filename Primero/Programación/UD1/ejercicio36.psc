Algoritmo ejercicio36
	Escribir "Inserta una cantidad de dinero:"
	Leer dinero
	euros <- trunc(dinero)
	centimos <- (dinero-euros)*100
	Escribir dinero, " son ", euros, " euros y ", centimos, " centimos"
FinAlgoritmo
