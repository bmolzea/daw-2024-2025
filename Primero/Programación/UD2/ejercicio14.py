escala = input("Elige escala (Celsius o Fahrenheit): ")
temperatura = float(input("Introduce la temperatura: "))

if escala == "Celsius":
    conversion = temperatura*9/5+32
    print(f"{temperatura} grados Celsius es {conversion} grados Fahrenheit")
elif escala == "Fahrenheit":
    conversion = (temperatura-32)*5/9
    print(f"{temperatura} grados Fahrenheit es {conversion} grados Celsius")
else:
    print("La escala indicado no existe")