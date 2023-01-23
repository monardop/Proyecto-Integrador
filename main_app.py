import tkinter as tk
from tkinter import messagebox
import time
import sqlite3
import requests
import sys
 
##########################


def guardar_encargado(data):
    datosIn = (data["nombre"],data["ingreso"],"IN",0)
    datosOut = (data["nombre"],data["egreso"],"OUT",data["facturado"])
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosIn)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosOut)
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE registro 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encargado TEXT,
            fecha TEXT,
            evento TEXT,
            caja REAL
        )
        """)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosIn)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosOut)
    conn.commit()
    conn.close

 
def guardarVentas(data):
    datos = tuple(data)
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO ventas VALUES (null,?,?,?,?,?,?,?)", datos)
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE ventas 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            fecha TEXT,
            ComboS INT,
            ComboD INT,
            ComboT INT,
            Flurby INT,
            total REAL
        )
        """)
        cursor.execute("INSERT INTO ventas VALUES (null,?,?,?,?,?,?,?)", datos)
    conn.commit()
    conn.close

def cotizar():
    try:
        r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolaroficial")
        valor = r.json()["venta"]
        valor = round(float(valor))
        return valor
    except:
        messagebox.showerror(title="Error grave", message="Sin internet para cotizar. Terminado")
        sys.exit()


def validar(dato):
	try:
		dato = int(dato)
		return dato
	except ValueError:
		return -1
 
 
def borrar():
    c_comboUno.delete(0,tk.END)
    c_comboDos.delete(0,tk.END)
    c_comboTres.delete(0,tk.END)
    c_postre.delete(0,tk.END)
    c_cliente.delete(0,tk.END)


def cancelar_pedido():
	respuesta = messagebox.askyesno(title="Pregunta", message="Desea cancelar el pedido?")
	if respuesta:
		borrar()


 
def pedir():
    cantUno= c_comboUno.get()
    cantUno = validar(cantUno)
    cantDos = c_comboDos.get()
    cantDos = validar(cantDos)
    cantTres = c_comboTres.get()
    cantTres = validar(cantTres)
    cantPostre = c_postre.get()
    cantPostre = validar(cantPostre) 
    dolar = cotizar() 
    if cantUno>=0 and cantDos>=0 and cantTres>=0 and cantPostre>=0:
        cliente = c_cliente.get()
        encargado = c_encargado.get()
        if cliente and encargado:
            respuesta = messagebox.askyesno(title="Pregunta", message="¿Confirma el pedido?")
            if respuesta:
                costot = ((cantUno*precios["ComboSimple"])+(cantDos*precios["ComboDoble"])+(cantTres*precios["ComboTriple"])+(cantPostre*precios["Flurby"]))
                totalPesos = costot * dolar
                fecha = time.asctime()
                pedido = [cliente,fecha,cantUno,cantDos,cantTres,cantPostre,totalPesos]
                messagebox.showinfo(title="A pagar", message="$"+str(totalPesos))
                guardarVentas(pedido)
                messagebox.showinfo(title="Información", message="Pedido Exitoso")
                if  datos_encargado["nombre"] != encargado and datos_encargado["egreso"] == "" : # cuando inicia la app egreso es vacio
                    datos_encargado["nombre"] = encargado
                    datos_encargado["egreso"] = "SinFecha" # es solo para que la proxima no cumpla la condición, es solo al inicio
                    datos_encargado["facturado"] += totalPesos #voy incrementando totales
                elif datos_encargado["nombre"] == encargado:
                    datos_encargado["facturado"] += totalPesos #voy incrementando totales
                else:
                    datos_encargado["egreso"] = fecha # al cambiar de encargado registro la fecha
                    guardar_encargado(datos_encargado) # guardo
                    #borramos el encargado anterior, en el diccionario ponemos el nuevo
                    datos_encargado["nombre"] = encargado # iniciamos el nuevo encargado
                    datos_encargado["Ingreso"] = fecha
                    datos_encargado["facturado"] = 0
                    datos_encargado["facturado"] += totalPesos
                borrar()
            else:
                messagebox.showinfo(title="Información", message="Pedido en pausa")
        else:
            messagebox.showwarning(title="Advertencia", message="Error, ingrese bien los datos")
    else:
        messagebox.showwarning(title="Advertencia", message="Error, ingrese datos correctos")
 

def salir():
    #salir seguro implica guardar el último encargado
    respuesta = messagebox.askyesno(title="Pregunta", message="¿Desea salir?")
    if respuesta:
        datos_encargado["egreso"] = time.asctime()
        guardar_encargado(datos_encargado)
        sys.exit()
    

 
# -----------------------------------------------------------

precios = {"ComboSimple":5,"ComboDoble":6,"ComboTriple":7,"Flurby":2}
datos_encargado = {"nombre":"","ingreso":time.asctime(),"egreso":"","facturado":0}
 
# -------------------------------------------------------------------
 
ventana = tk.Tk()
ventana.config(width = 400, height = 400)
ventana.title("Delivery")
 
# etiquetas ------------------------------------------------------------
ebienvenido = tk.Label(text="------ Pedidos -------")
ebienvenido.place(x = 140, y = 20)

enombreEncargado = tk.Label(text = "Nombre Encargado : ")
enombreEncargado.place(x = 50, y = 70)
ecomboUno = tk.Label(text = "Combo S cantidad : ")
ecomboUno.place(x = 50, y = 110)
ecomboDos = tk.Label(text = "Combo D cantidad : ")
ecomboDos.place(x = 50, y = 150)
ecomboTres = tk.Label(text = "Combo T cantidad : ")
ecomboTres.place(x = 50, y = 190)
ecliente = tk.Label(text = "Postre cantidad : ")
ecliente.place(x = 50, y = 230)
epostre = tk.Label(text = "Nombre del cliente : ")
epostre.place(x = 50, y = 270)
 
#####cajas#########

c_encargado = tk.Entry()
c_encargado.place(x = 230, y = 70)
c_comboUno = tk.Entry()
c_comboUno.place(x = 230, y = 110)
c_comboDos = tk.Entry()
c_comboDos.place(x = 230, y = 150)
c_comboTres = tk.Entry()
c_comboTres.place(x = 230, y = 190)
c_postre = tk.Entry()
c_postre.place(x = 230, y = 230)
c_cliente = tk.Entry()
c_cliente.place(x = 230, y = 270)
 
##### Botones #########
 
b_pedido = tk.Button(text = "Hacer Pedido", command = pedir)
b_pedido.place(x = 270 , y = 330, height=40, width = 100)
 
b_cancelar = tk.Button(text = "Cancelar Pedido", command = cancelar_pedido)
b_cancelar.place(x = 150 , y = 330, height=40, width = 100)
 
b_info = tk.Button(text = "Salir seguro",command=salir)
b_info.place(x = 30 , y = 330, height=40, width = 100)
 
 
ventana.mainloop()