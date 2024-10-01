Algoritmo ejercicio24
	Escribir "Inserte su nombre:"
	Leer nombre
	Escribir "Inserta tu contraseña:"
	Leer pass1
	Escribir "Vuelve a repetir tu contraseña:"
	Leer pass2
	Mientras pass1 <> pass2 Hacer
		Escribir "Las constraseñas no son iguales"
		Escribir "Inserta tu contraseña:"
		Leer pass1
		Escribir "Vuelve a repetir tu contraseña:"
		Leer pass2
	Fin Mientras
	Escribir "Usuario creado correctamente"
FinAlgoritmo
