from tkinter import messagebox
import datetime
import sys
import ventas
import gui
import funciones_botones as fb


##############################################

def cancelar():
    rta = fb.cartel_confirma()
    if rta == 1:
        fb.borrar_campos()

def salir():
    rta = fb.cartel_confirma()
    
            
def confirmar():
    pass