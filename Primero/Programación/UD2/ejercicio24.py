nombreUsuario = input("Introduce tu nombre de usuario: ")
contrasnhaCorrecta = False

while not contrasnhaCorrecta:
    pass1 = input("Introduce tu contraseña: ")
    pass2 = input("Introduce de nuevo tu contraseña: ")
    if pass1 == pass2:
        contrasnhaCorrecta = True
    else:
        print("Las contraseñas no coinciden")

print("Usuario creado correctamente")

