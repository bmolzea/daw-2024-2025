Algoritmo ejercicio24
	Escribir "Inserte su nombre:"
	Leer nombre
	Escribir "Inserta tu contrase�a:"
	Leer pass1
	Escribir "Vuelve a repetir tu contrase�a:"
	Leer pass2
	Mientras pass1 <> pass2 Hacer
		Escribir "Las constrase�as no son iguales"
		Escribir "Inserta tu contrase�a:"
		Leer pass1
		Escribir "Vuelve a repetir tu contrase�a:"
		Leer pass2
	Fin Mientras
	Escribir "Usuario creado correctamente"
FinAlgoritmo
