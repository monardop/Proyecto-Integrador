import tkinter
from functools import partial #me permite crear funciones de orden superior
from datetime import datetime
import sqlite3

def current_datatime():
    """
    -Esta funcion retorna la fecha y hora para anexar al registro y a las ventas.
    -This function returns date and time to index into the sells and IN/OUT register.
    """
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
    