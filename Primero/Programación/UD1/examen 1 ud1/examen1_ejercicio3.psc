Algoritmo examen1_ejercicio3
	Repetir
		Escribir "¿Qué operación quieres realizar?"
		Escribir "1. Suma"
		Escribir "2. Resta"
		Escribir "3. Multiplicación"
		Escribir "4. División"
		Escribir "5. Resto"
		Escribir "0. Salir"
		Leer seleccion
		Si seleccion>=1 Y seleccion<=5 Entonces
			Escribir "Inserta el primer número: "
			Leer num1
			Escribir "Inserta el segundo número: "
			Leer num2
		Fin Si
		Segun seleccion Hacer
			1:
				Escribir num1," + ",num2," = ",num1+num2
			2:
				Escribir num1," - ",num2," = ",num1-num2
			3:
				Escribir num1," x ",num2," = ",num1*num2
			4:
				Escribir num1," / ",num2," = ",num1/num2
			5:
				Escribir "El resto de dividir ",num1," entre ",num2," es ", num1 MOD num2
		Fin Segun
	Hasta Que seleccion = 0
FinAlgoritmo
