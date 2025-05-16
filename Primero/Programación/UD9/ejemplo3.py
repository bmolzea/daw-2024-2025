import tkinter as tk

class CalculadoraApp:
    def __init__(self, root):
        self.expresion = ""

        root.title("Calculadora")
        root.geometry("300x400")
        root.resizable(False, False)

        self.entrada = tk.Entry(root, font=("Arial", 20), justify="right", bd=5, relief=tk.RAISED)
        self.entrada.pack(fill="both", padx=10, pady=10)

        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        boton_frame = tk.Frame(root)
        boton_frame.pack(expand=True, fill="both", padx=10, pady=10)

        for i, fila in enumerate(botones):
            boton_frame.columnconfigure(i, weight=1)
            boton_frame.rowconfigure(i, weight=1)
            for j, texto in enumerate(fila):
                b = tk.Button(boton_frame, text=texto, font=("Arial", 18),
                              command=lambda t=texto: self.pulsar(t))
                b.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)


    def pulsar(self, tecla):
        if tecla == "C":
            self.expresion = ""
            self.actualizar_entrada()
        elif tecla == "=":
            try:
                resultado = str(eval(self.expresion))
                self.expresion = resultado
            except Exception:
                self.expresion = "ERROR"
            self.actualizar_entrada()
        else:
            self.expresion += tecla
            self.actualizar_entrada()

    def actualizar_entrada(self):
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, self.expresion)

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
