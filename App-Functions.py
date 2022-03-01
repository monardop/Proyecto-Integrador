import enum
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
    
    def __init__(self, nombre: str, cS: int, cD: int, cT: int, pos: int):

        self.cliente = nombre
        self.comboS = cS
        self.comboD = cD
        self.comboT = cT
        self.postre = pos
        
        def obtener_datos(self, cS: int, cD: int, cT: int, pos: int):
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
            lista = [0]
            for i,j in enumerate(self.comboS, self.comboD, self.comboT, self.postre):
                lista[i] = j
            for i,j in enumerate(lista):
                lista[i] = j*valor
                total += lista[i]
            messagebox.showinfo(title="Compra realizada", message=f"La compra fue realizada. El total es de ${total} ARS")
            return total
        def cargar_venta(cliente:str, s: float,d: float,t: float,p: float,total: float): #esta funcion va a cargar el registro de ventas (base de datos)
            fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
            conn = sqlite3.connect('comercio.sqlite')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ventas VALUES(?,?,?,?,?,?,?,?)", (cliente,fecha, s,d,t,p,total))
            conn.commit()
            conn.close()

        obtener_datos(cS,cD,cT,pos)
        self.total = total_venta()
        cargar_venta(self.cliente, self.comboS, self.comboD, self.comboT, self.postre, self.total)
    