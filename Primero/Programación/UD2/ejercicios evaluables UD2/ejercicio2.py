import random

nPares = 0

for _ in range(10):
    aleatorio = random.randint(20, 40)
    print(aleatorio)

    if aleatorio % 2 == 0:
        nPares += 1


porcentajePares = nPares / 10 * 100
porcentajeImpares = 100 - porcentajePares

print(f"Un {porcentajePares}% son pares y un {porcentajeImpares}% son impares")
