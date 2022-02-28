import tkinter as tk
from tkinter import messagebox
import datetime
import sqlite3
import requests
import sys
class Vendedor():
    def __init__(self):
        """
        Cada vendedor puede tener múltiples ventas, por lo que tomo a cada vendedor como un objeto.
        En esta clase se iniciará en el registro de entrada y salida la entrada del vendedor. Luego se cargaran x ventas. Por último se cargará nuevamente el registro de E/S con la salida.
        Tendrá 3 funciones: registro, sumatoria de ventas y obtención de fecha y hora (para el registro)
        """
        pass

class Venta():
    """
    Cada venta será tratada como un objeto para facilitar el trabajo del vendedor. 
    """
    def __init__(self, nombre, cS, cD, cT, pos):
    
        def obtener_datos(self, cS, cD, cT, pos):
            self.comboS = cS*5
            self.comboD = cD*6
            self.comboT = cT*7
            self.postre = pos*2

        def convertir_pesos():
            #Utilizo una api externa para obtener el precio dolar-peso
            try:
                r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolaroficial")
                valor = r.json()["venta"]
                valor = round(float(valor))
                return valor   
            except:
                messagebox.showerror(title="Error", message="Error en el cambio de moneda")
                sys.exit()

        def total_venta():
            #uso el valor obtenido del dolar-peso para transformar el precio de las ventas a pesos.    
            valor = convertir_pesos()
            self.comboS, self.comboD, self.comboT, self.postre *= valor
            total = self.comboS + self.comboD + self.comboT + self.postre
            return total
        def cargar_venta(): #esta funcion va a cargar el registro de ventas (base de datos)
            pass
        
        self.cliente = nombre
        obtener_datos(cS,cD,cT,pos)
        self.total = total_venta()
        messagebox.showinfo(title="Compra realizada", message=f"La compra fue realizada. El total es de ${self.total} ARS")
    
def current_datatime():
    message = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    return message

def pedido_sumatoria(cS, cD, cT, pos):
    comboS = (cS.get())*5
    comboD = (cD.get())*6
    comboT = (cT.get())*7
    postre = (pos.get())*2
    total = comboS + comboD + comboT + postre
    return total

def boton_pedido(en, cS, cD, cT, pos, cli):
    encargado_actual = "Nuevo"
    
    if encargado_actual == "Nuevo":
        encargado_actual = en
        totalGeneral = 0
    else:
        if encargado_actual != en:
            #aca crearia el registro de salida del empleado anterior.
            totalGeneral = 0
    nuevo_ingreso = pedido_sumatoria(cS, cD, cT, pos)
    #aca cargo la venta al registro de ventas.
    totalGeneral += nuevo_ingreso
    