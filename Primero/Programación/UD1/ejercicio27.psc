Algoritmo ejercicio27
	numSecreto <- 25
	nIntentos <- 1
	Escribir "Intenta adivinar el número:"
	Repetir
		Leer numElegido
		Si numElegido <> numSecreto Entonces
			nIntentos <- nIntentos + 1
			Si numElegido > numSecreto Entonces
				Escribir "Has fallado, el número es menor, vuelve a intentarlo:"
				
			SiNo
				Escribir "Has fallado, el número es mayor, vuelve a intentarlo:"
			Fin Si
		Fin Si
		
	Hasta Que numElegido = numSecreto
	Escribir "Enhorabuena has acertado, has tardado: ",nIntentos," intentos" 	
	
	
FinAlgoritmo
