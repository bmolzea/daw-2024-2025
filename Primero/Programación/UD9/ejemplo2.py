import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.contador = 0

        root.title("Contador simple")
        root.geometry("300x150")
        root.resizable(True, True)

        self.label_valor = tk.Label(root, text=str(self.contador), font=("Arial", 24))
        self.label_valor.pack(pady=10)

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack()

        self.boton_sumar = tk.Button(self.frame_botones, text="Sumar +1", command=self.sumar, width=10)
        self.boton_sumar.grid(row=0, column=0, padx=5)

        self.boton_restar = tk.Button(self.frame_botones, text="Restar -1", command=self.restar, width=10, state="disabled")
        self.boton_restar.grid(row=0, column=1, padx=5)

    def actualizar_label(self):
        self.label_valor.config(text=str(self.contador))

    def sumar(self):
        self.contador += 1
        if self.contador == 1:
            self.boton_restar.config(state="normal")
        self.actualizar_label()

    def restar(self):
        if self.contador > 0:
            self.contador -= 1
            if self.contador == 0:
                self.boton_restar.config(state="disabled")
            self.actualizar_label()

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()
