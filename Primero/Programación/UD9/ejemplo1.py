import tkinter as tk

class HolaMundoApp:
    def __init__(self, root):
        root.title("Hola Mundo")
        root.geometry("300x100")
        root.resizable(True, True)

        self.etiqueta = tk.Label(root, text="¡Hola, mundo!", font=("Arial", 18))
        self.etiqueta.pack(pady=20)

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = HolaMundoApp(root)
    root.mainloop()