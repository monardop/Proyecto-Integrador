from tkinter import *
from tkinter import messagebox
import datetime
import sys
import ventas
import gui
import sqlite3

def borrar_campos():
    gui.cS.delete()
    gui.cD.delete()
    gui.cT.delete()
    gui.pos.delete()
    gui.cli.delete()

def cartel_confirma():
    rta = messagebox.askquestion(message="¿Está seguro?")
    if rta == "yes":
        return 1
    else:
        return 0

def cheq_vendedor():
    vendedor = str(gui.en.get())
    with open("Vendedor.txt", "r") as f:
        vendedor_anterior = f.read()
    if vendedor != vendedor_anterior:
        with open("Vendedor.txt", "w") as f:
            f.write(vendedor)
        return 0
    else:
        return 1
def cerrar_app():
    vendedor = str(gui.en.get())
    with open("Vendedor.txt", "w") as f:
        f.write(vendedor)
    messagebox.showinfo(title="Salir", message="Cerrando app")
    sys.exit()

def llenar_registro(self, op: str, vendedor: str, total: float):
    #Esta función llena el registro de entrada y salida de vendedores.
    date = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    conn = sqlite3.connect('comercio.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registro VALUES(?,?,?,?)", (op, date, vendedor, total))
    conn.commit()
    conn.close()

def control_validez(x):

    if x is isinstance(x, int):
        if x < 0: 
            return 1
    else:
        return 1
def crear_venta():
    """Con la variable x creo una bandera para identificar si hubo un error al cargar los datos, dado que estos serán ingresados de forma manual y estos no pueden ser algo distinto de un entero positivo.
    Una vez comprobado los datos, creo el objeto venta que se encarga de obtener precios y cargarlos al servidor. De este objeto me llevo el total de esa venta."""
    comboS = gui.cS.get()
    x = control_validez(comboS)
    comboD = gui.cD.get()
    x = control_validez(comboD)
    comboT = gui.cT.get()
    x = control_validez(comboT)
    postre = gui.pos.get()
    x = control_validez(postre)
    cliente = str(gui.cli.get())
    if x != 1:
        venta = ventas.Venta(cliente, comboS,comboD,comboT,postre)
        return venta.total
    else:
        messagebox.showerror(title="Erorr", message="Error al ingresar datos")
        return 1 