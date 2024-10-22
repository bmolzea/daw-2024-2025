ganancias = float(input("¿Cuánto dinero has ganado?"))

if ganancias <= 10000:
    hacienda = 0
elif ganancias > 10000 and ganancias <= 20000:
    exceso = ganancias - 10000
    hacienda = exceso * 0.1
elif ganancias > 20000 and ganancias <= 40000:
    exceso = ganancias - 20000
    hacienda = 10000 * 0.1 + 0.2 * exceso
else:
    exceso = ganancias - 40000
    hacienda = 1000 + 2000 + exceso * 0.3

print(f"Hacienda somos todos, nos debes: {hacienda}€")