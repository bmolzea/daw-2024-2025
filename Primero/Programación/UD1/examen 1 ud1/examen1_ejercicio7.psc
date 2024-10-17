Algoritmo examen1_ejercicio7
	puntosHumano <- 0
	puntosBot <- 0
	ronda <- 1
	Repetir
		Escribir "====== RONDA",ronda," ======"
		Escribir  "Elige tu jugada: "
		Leer jugadaHumano
		jugadaBotCodigo <- Azar(3)
		Segun jugadaBotCodigo Hacer
			0:
				jugadaBot <- "Piedra"
			1:
				jugadaBot <- "Papel"
			2:
				jugadaBot <- "Tijera"
		Fin Segun
		Escribir "El bot ha elegido: ",jugadaBot
		Segun jugadaHumano Hacer
			"Piedra":
				Segun jugadaBot Hacer
					"Piedra":
						resultado <- 0
					"Tijera":
						resultado <- 1
					"Papel":
						resultado <- -1
				Fin Segun
			"Papel":
				Segun jugadaBot Hacer
					"Piedra":
						resultado <- 1
					"Tijera":
						resultado <- -1
					"Papel":
						resultado <- 0
				Fin Segun
			"Tijera":
				Segun jugadaBot Hacer
					"Piedra":
						resultado <- -1
					"Tijera":
						resultado <- 0
					"Papel":
						resultado <- 1
				Fin Segun
		Fin Segun
		Segun resultado Hacer
			-1:
				Escribir "Has perdido :("
				puntosBot <- puntosBot + 1
			0:
				Escribir "Empate"
			1:
				Escribir "Has ganado!!!!"
				puntosHumano <- puntosHumano + 1
		Fin Segun
		ronda <- ronda + 1
	Hasta Que puntosHumano = 3 O puntosBot = 3
	Si puntosHumano = 3 Entonces
		Escribir "Has ganado máquina, leyenda!!!!!"
	SiNo
		Escribir "Has perdido, eres una decepción para el género humano"
	Fin Si
FinAlgoritmo
