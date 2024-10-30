i = 0

while True:
    num = int(input("Introduce un número: "))

    if i == 0:
        numMin = num
        numMax = num

    if num == 0:
        break

    if num > numMax:
        numMax = num

    if num < numMin:
        numMin = num
    
    i = i + 1

print(f"El número máximo es {numMax} y el mínimo es {numMin}")
    