Algoritmo examen1_ejercicio6
	Escribir "Inserta tu nombre de usuario: "
	Leer usuario
	Repetir
		Escribir "Inserta tu contrase�a: "
		Leer pass1
		Mientras Longitud(pass1) < 8 Hacer
			Escribir "La constrase�a debe tener 8 o m�s caracteres"
			Escribir "Inserta tu contrase�a"
			Leer pass1
		Fin Mientras
		Escribir "Repite tu contrase�a"
		Leer pass2
		Si pass1 <> pass2 Entonces
			Escribir "Las contrase�as no coinciden. Vuelve a insertarlas."
		Fin Si
	Hasta Que pass1 = pass2
	Escribir "Usuario creado correctamente"
	Escribir "Usuario: ",usuario
	Escribir "Contrase�a: ",pass1
FinAlgoritmo
