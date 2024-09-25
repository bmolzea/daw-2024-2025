Algoritmo ejercicio20
	Escribir "Cuánto pesa tu coche?(kg)"
	Leer peso
	Si peso<1000 Entonces
		Escribir "Es un coche ligero"
	SiNo
		Si peso>=1000 Y peso<2000 Entonces
			Escribir "Es un coche medio"
		SiNo
			Escribir "Es un coche pesado"
		Fin Si
	Fin Si
FinAlgoritmo
