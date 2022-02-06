from tkinter import *
from tkinter.ttk import Style

class App(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Delivery")
        self.master.config(padx=20, pady=20) #agrego un poco de padding a la ventana


        #configure the grid
        self.columnconfigure(0, pad=10)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=10)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=50)


        #crea las leyendas
        titulo = Label(self, text="-------Pedidos-------", pady=10).grid(row=0, column=2)
        encargado = Label(self, text="Nombre del encargado").grid(column=1)
        comboS = Label(self, text="Combo simple").grid(column=1)
        comboD = Label(self, text="Combo doble").grid(column=1)
        comboT = Label(self, text="Combo triple").grid(column=1)
        postre = Label(self, text="Postre").grid(column=1)
        cliente = Label(self, text="Nombre del cliente").grid(column=1)

        #text input
        #Entry es un label que permite ingresar texto en pequeñas cantidades
        en = Entry(self, width=15).grid(column=3, row=1)
        cS = Entry(self, width=15).grid(column=3, row=2)
        cD = Entry(self, width=15).grid(column=3, row=3)
        cT = Entry(self, width=15).grid(column=3, row=4)
        pos = Entry(self, width=15).grid(column=3, row=5)
        cli = Entry(self, width=15).grid(column=3, row=6)

        #botones
        salida = Button(self, text="Salir", width=15, pady=5)
        salida.grid(row=7, column=1)
        cancel = Button(self, text="Cancelar pedido", width=15, pady=5)
        cancel.grid(row=7, column=2)
        submit = Button(self, text="Hacer pedido", width=15, pady=5).
        submit.grid(row=7, column=3)

        self.pack()

def main():
    root = Tk() #creo la ventana
    app = App()
    root.mainloop()

if __name__ == '__main__':
    main()


