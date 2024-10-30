menor = int(input("Introduce un número: "))
mayor = int(input("Introduce otro número: "))

# No incluyendo el primer ni último número
for i in range(menor+1, mayor):
    print(i)