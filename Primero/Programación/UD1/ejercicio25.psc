Algoritmo ejercicio25
	numSecreto <- 25
	Escribir "Intenta adivinar el número:"
	Leer numElegido
	nIntentos <- 1
	Mientras numElegido <> numSecreto Hacer
		Escribir "Has fallado"
		Si numElegido > numSecreto Entonces
			Escribir "El número es menor"
		SiNo
			Escribir "El número es mayor"
		Fin Si
		Escribir "Intenta adivinar el número:"
		Leer numElegido
		nIntentos <- nIntentos + 1
	Fin Mientras
	Escribir  "Enhorabuena!!!, has acertado"
	Escribir "Has tardado:", nIntentos, " intentos"
FinAlgoritmo
