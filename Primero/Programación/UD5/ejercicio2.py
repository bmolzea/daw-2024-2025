agenda = {
    'Paco':     '600111222',
    'Paco Jr':  '600222333',
    'Paquete':  '600333444'
}

def mostrar_menu():
    print("""
--- AGENDA DE CONTACTOS ---
1. Añadir contacto
2. Buscar contacto
3. Listar contactos
4. Salir
""")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4)? ")

    if opcion == '1':
        nombre = input("Nombre? ")
        telefono = input("Teléfono? ")
        agenda[nombre] = telefono
        print(f"Contacto '{nombre}' guardado!\n")
    elif opcion == '2':
        nombre = input("Nombre a buscar? ")
        if nombre in agenda:
            print(f"{nombre}: {agenda[nombre]}\n")
        else:
            print(f"No existe ningún contacto llamado {nombre}")
    elif opcion == '3':
        if not agenda:
            print("La agenda está vacía")
        else:
            print("Contactos:")
            for nombre, telefono in agenda.items():
                print(f"\t - {nombre}: {telefono}")
            print()
    elif opcion == '4':    
        break
    else:
        print("Opción no válida. Elige entre 1 y 4.\n")






