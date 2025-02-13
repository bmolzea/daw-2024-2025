tareas = ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]

print("Bienvenido a la app to-do")
print("1. Ver tareas pendientes")
print("2. Agregar tarea")
print("0. Salir")

while True:
    opcion = input("Elige una opción: ")
    if opcion == "0":
        break
    
    if opcion == "1":
        if len(tareas) > 0:
            print("Tareas pendientes: ")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
            n_tarea = int(input("Has completado alguna tarea?"))
            if n_tarea > 0 and n_tarea < len(tareas)+1:
                tareas.pop(n_tarea-1)
                print("Eres un crack!!!")
            elif n_tarea > len(tareas)+1:
                print("Tarea no válida")
        else:
            print("No hay tareas")
    elif opcion == "2":
        tarea = input("Inserta una tarea: ")
        pos = int(input("Posición: "))
        while pos < 1:
            pos = int(input("Posición no válidad, pon una válida: "))
        tareas.insert(pos-1, tarea)