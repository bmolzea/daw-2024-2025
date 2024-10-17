Algoritmo examen1_ejercicio6
	Escribir "Inserta tu nombre de usuario: "
	Leer usuario
	Repetir
		Escribir "Inserta tu contraseña: "
		Leer pass1
		Mientras Longitud(pass1) < 8 Hacer
			Escribir "La constraseña debe tener 8 o más caracteres"
			Escribir "Inserta tu contraseña"
			Leer pass1
		Fin Mientras
		Escribir "Repite tu contraseña"
		Leer pass2
		Si pass1 <> pass2 Entonces
			Escribir "Las contraseñas no coinciden. Vuelve a insertarlas."
		Fin Si
	Hasta Que pass1 = pass2
	Escribir "Usuario creado correctamente"
	Escribir "Usuario: ",usuario
	Escribir "Contraseña: ",pass1
FinAlgoritmo
