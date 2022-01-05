from os import system
from datetime import datetime

def current_datatime()
    now = datetime.now()
    hoy = date(now.year, now.month, now.day).ctime()
    fecha = hoy.split()
    message = now.strftime(f"{fecha[0]} {fecha[1]} %d %H:%M:%S %Y")
    return message

def in_out_Register(op, name, s, d, t, total):
    todayDate = current_datatime()
    if op == 1:
        with open("ventas.txt", "a") as f:
            f.write(f"{name}; {todayDate}; {s}; {d}; {t}; ${total}")
    elif op == 2:
        with open("registros.txt", "a") as f:
            f.write(f"IN {todayDate}; Encargad@: {name}")
    
    elif op == 3:
        with open("registros.txt", "a") as f:
            f.write(f"OUT {todayDate}; Encargad@: {name} ${total}")
    



def welcome():
    print("Bienvenido a Hamburguesas IT")
    name = input("Ingrese su nombre encargad@: ")
    print(f"\nHamburguesas IT\nEncargad@ → {name}")
    print("Recuerda recibir siemre al cliente con una sonrisa :) \n")
    return name

def operation():
    while True:
        op = int(input("1 - Ingreso nuevo pedido\n2 - Cambio de turno\n3 - Apagar sistema\n"))
        if not isinstance(op, int) or (op<1 or op>3):
            print("El valor ingresado es incorrecto")
        else:
            break
    return op
    
def main():
    name = welcome()
    op = operation()
    
    system("pause")



main()