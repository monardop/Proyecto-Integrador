from tkinter import *
from tkinter import messagebox
import datetime
import sys
import ventas
import gui
import sqlite3

###################################################################

def borrar_campos():
    gui.cS.delete()
    gui.cD.delete()
    gui.cT.delete()
    gui.pos.delete()
    gui.cli.delete()

def cartel_confirma(op: str):
    rta = messagebox.askquestion(message="¿Está seguro?", title= op)
    if rta == "yes":
        return 1
    else:
        return 0

def cheq_vendedor():
    #Esta función chequea que el vendedor anterior sea el mismo que en el nuevo pedido. De serlo, se suma el total. En caso contrario, se envía los datos para llenar registro. 
    
    vendedor = str(gui.en.get())
    if vendedor == "":
        messagebox.showerror(title="Error", message="No ingresó el nombre de vendedor")
        return 1

    try:
        with open("Vendedor.txt", "r") as f:
            vendedor_anterior = f.read()
    except FileNotFoundError:
        with open("Vendedor.txt", "w") as f:
            f.write(vendedor)
        with open("ventaTotal.txt", "w") as f:
                f.write("0")
        vendedor_anterior = vendedor
    

    if vendedor != vendedor_anterior:
        try:
            with open("ventaTotal.txt", "r") as f:
                total = float(f.read())
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Ha ocurrido un error.")
            return 1
        llenar_registro("OUT", vendedor_anterior, total)  
        llenar_registro("IN", vendedor, 0)
        with open("Vendedor.txt", "w") as f:
            f.write(vendedor)
        with open("ventaTotal.txt", "w") as f:
            f.write("0")
        return 0
    else:
        return 0


def cerrar_app():
    #Funcion del boton salir. Básicamente crea un .txt que guardara el nombre del ultimo vendedor 
    vendedor = str(gui.en.get())
    with open("Vendedor.txt", "w") as f:
        f.write(vendedor)
    messagebox.showinfo(title="Salir", message="Cerrando app")
    sys.exit()

def llenar_registro( op: str, vendedor: str, total: float):
    #Esta función llena el registro de entrada y salida de vendedores.
    date = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    conn = sqlite3.connect('comercio.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registro VALUES(?,?,?,?)", (op, date, vendedor, total))
    conn.commit()
    conn.close()

def control_validez(x, elem: str):
    """Con esta función controlo que lo ingresado en los campos de pedidos sean nros enteros no negativos."""
    if x is isinstance(x, int):
        if x <= 0: 
            return 1
    else:
        messagebox.showerror(title="Error", message=f"Error en el ingreso de datos en {elem}")
        return 1


def crear_venta():
    """Con la variable x creo una bandera para identificar si hubo un error al cargar los datos, dado que estos serán ingresados de forma manual y estos no pueden ser algo distinto de un entero positivo.
    Una vez comprobado los datos, creo el objeto venta que se encarga de obtener precios y cargarlos al servidor. De este objeto me llevo el total de esa venta."""
    comboS = gui.cS.get()
    x = control_validez(comboS, "Combo Simple")
    comboD = gui.cD.get()
    x = control_validez(comboD, "Combo doble")
    comboT = gui.cT.get()
    x = control_validez(comboT, "Combo triple")
    postre = gui.pos.get()
    x = control_validez(postre, "Postre")
    cliente = str(gui.cli.get())
    if cliente == "":
        messagebox.showerror(title="Error", message="Error en el ingreso de datos de cliente")
        x = 1
    if x != 1:
        venta = ventas.Venta(cliente, comboS,comboD,comboT,postre)
        return venta.total
    else:
        return -1 

def suma_ventas(total: float):
    with open("ventaTotal.txt", "w") as f:
        antes = float(f.read())
        total += antes
        f.write(total)


