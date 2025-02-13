andalucia_oriental = ["Granada", "Jaén", "Almería", "Málaga"]
andalucia_occidental = ["Sevilla", "Cádiz", "Huelva", "Córdoba"]
andalucia = []
andalucia.extend(andalucia_occidental)
andalucia.extend(andalucia_oriental)
# También podemos utilizar el operador suma
andalucia2 = andalucia_occidental + andalucia_oriental 
print(andalucia)
print(andalucia2)