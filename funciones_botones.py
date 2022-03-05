import tkinter
from tkinter import messagebox
import datetime
import sys
import ventas
import gui

def borrar_campos():
    gui.cS.delete()
    gui.cD.delete()
    gui.cT.delete()
    gui.pos.delete()

def cartel_confirma():
    rta = messagebox.askquestion(message="¿Está seguro?")
    if rta == "yes":
        return 1
    else:
        return 0

def cheq_vendedor(vendedor_actual: str):
    vendedor = gui.en.get()
    if vendedor != vendedor_actual:
        return 1
    else:
        return 0
    

