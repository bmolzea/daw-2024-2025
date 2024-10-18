altura = float(input("Introduce tu altura: "))
peso = float(input("Introduce tu peso: "))
imc = peso / (altura**2)
print(f"Tu imc es: {imc}")
if imc<18.5:
    print("Tienes bajo peso")
elif imc>=18.5 and imc<24.9:
    print("Tienes un buen peso")
elif imc>=24.9 and imc<29.9:
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")


