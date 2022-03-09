from tkinter import messagebox
import datetime
import sys
import ventas
import gui
import funciones_botones as fb


##############################################

def cancelar():
    rta = fb.cartel_confirma("Cancelar pedido")
    if rta == 1:
        fb.borrar_campos()

def salir():
    rta = fb.cartel_confirma("Salir de la app")
    if rta == 1:
        fb.cerrar_app()
            
def confirmar():
    vendedor = fb.cheq_vendedor() 
    if vendedor == 0:
        total = fb.crear_venta()
        if total != (-1):
            fb.suma_ventas(total)
            messagebox.showinfo(title="Venta confirmada", message=f"La venta fue exitosa con un total de ${total}")
            fb.borrar_campos()

