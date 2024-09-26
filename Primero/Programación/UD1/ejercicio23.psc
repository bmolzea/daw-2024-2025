Algoritmo ejercicio23
	porteros<-"Iker Casillas y Victor Valdes"
	defensas<-"Pique, Puyol, Sergio Ramos y Capdevilla"
	centrocampistas<-"Xavi, Xabi e Iniesta"
	delanteros<-"Villa, Raúl y Lamine"
	Escribir "¿Los jugadores de qué posición quieres saber?"
	Leer posicion
	Segun posicion Hacer
		"Porteros":
			Escribir porteros
		"Defensas":
			Escribir defensas
		"Centrocampistas":
			Escribir centrocampistas
		"Delanteros":
			Escribir delanteros
		De Otro Modo:
			Escribir "No has indicado una posición correcta"
	Fin Segun
FinAlgoritmo
