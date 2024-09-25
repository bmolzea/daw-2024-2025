Algoritmo ejercicio21
	Escribir "Dime tu altura(en metros):"
	Leer altura
	Escribir "Dime tu peso(en kg):"
	Leer peso
	imc<-peso/(altura*altura)
	Escribir "Tu imc es:", imc, " por lo tanto:"
	Si imc<18.5 Entonces
		Escribir  "Tienes bajo peso"
	SiNo
		Si imc>=18.5 Y imc<24.9 Entonces
			Escribir "Tienes un buen peso"
		SiNo
			Si imc>=24.9 Y imc<29.9 Entonces
				Escribir "Tienes sobrepeso"
			SiNo
				Escribir "Tienes obesidad"
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
