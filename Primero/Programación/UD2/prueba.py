numCorrecto = False
while not numCorrecto:
    num = int(input("Introduce num de 1 a 10:"))
    if num>=1 and num<=10:
        numCorrecto = True

# vs

while True:
    num = int(input("Introduce num de 1 a 10:"))
    if num>=1 and num<=10:
        break