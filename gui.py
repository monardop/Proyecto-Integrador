from tkinter import *

root = Tk() #creo la ventana
root.title("Delivery")

#label muestra texto
titulo = Label(root, text="-------Pedidos-------", fg="white", bg= "red").grid(row=0, column=2)
encargado = Label(root, text="Nombre del encargado").grid(column=1)
comboS = Label(root, text="Combo simple").grid(column=1)
comboD = Label(root, text="Combo doble").grid(column=1)
comboT = Label(root, text="Combo triple").grid(column=1)
postre = Label(root, text="Postre").grid(column=1)
cliente = Label(root, text="Nombre del cliente").grid(column=1)

#Entry es un label que permite ingresar texto en pequeñas cantidades
en = Entry(root, width=10).grid(column=3, row=1)
cS = Entry(root, width=10).grid(column=3, row=2)
cD = Entry(root, width=10).grid(column=3, row=3)
cT = Entry(root, width=10).grid(column=3, row=4)
pos = Entry(root, width=10).grid(column=3, row=5)
cli = Entry(root, width=10).grid(column=3, row=6)

#botones
salida = Button(root, text="Salir").grid(row=7, column=1)
cancel = Button(root, text="Cancelar pedido").grid(row=7, column=2)
submit = Button(root, text="Hacer pedido").grid(row=7, column=3)

root.mainloop() #esto genera un loop infinito para que exista la ventana 