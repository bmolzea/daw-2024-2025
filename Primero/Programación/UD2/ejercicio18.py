cantidad = int(input("¿Cuántos productos has comprado? "))
precio = 8.75
if cantidad >= 1 and cantidad <= 10:
    total = precio * cantidad
elif cantidad >10 and cantidad <= 50:
    descuento = cantidad * precio * 0.05
    total = cantidad * precio - descuento
elif cantidad > 50 and cantidad <= 100:
    descuento = cantidad * precio * 0.1
    total = cantidad * precio - descuento
else:
    descuento = cantidad * precio * 0.15
    total = cantidad * precio - descuento

print(f"Tienes que pagar {total}€")