anho = int(input("Inserta un año: "))
if anho % 100 == 0:
    siglo = anho // 100
else:
    siglo = anho // 100 + 1

print(f"El año {anho} pertenece al siglo {siglo}")