from os import system, write
from datetime import datetime, date

def current_datatime():
    message = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    return message

def in_out_register(op, name, total):
    todayDate = current_datatime()
    if op == 1:
        with open("registros.txt", "a") as f:
            f.write(f"IN {todayDate}; Encargad@: {name}")
    
    elif op == 2:
        end_line = "#"
        with open("registros.txt", "a") as f:
            f.write(f"OUT {todayDate}; Encargad@: {name} ${total}")
            f,write(end_line*50)
    
def register_client(name, order, total):
    todayDate = current_datatime()
    s, d, t, p = order
    with open("ventas.txt", "a") as f:
                f.write(f"{name}; {todayDate}; {s}; {d}; {t}; {p}; ${total}")
    
def welcome():
    print("Bienvenido a Hamburguesas IT")
    name = input("Ingrese su nombre encargad@: ")
    print(f"\nHamburguesas IT\nEncargad@ → {name}")
    print("Recuerda recibir siemre al cliente con una sonrisa :) \n")
    return name

def operation():
    while True:
        op = input("1 - Ingreso nuevo pedido\n2 - Cambio de turno\n3 - Apagar sistema\n")
        
        if op.isdecimal() and op in ["1","2","3"]:
            op = int(op)
            break
        else:
            print("El valor ingresado es incorrecto")

    return op

def order_validation(type):
    while True:
        value = int(input(f"Ingrese cantidad de ordenes de {type}: "))
        if isinstance(value, int) and value>0:
            break
        else: 
            print("Su dato ingresado es incorrecto, por favor ingrese otra vez.")
    return value

def load_order():
    total = 0
    order = []
    while True:
        name = input("Ingrese nombre del cliente: ")
        s = order_validation("combo simple")
        total += s*5
        order.append(s)
        d = order_validation("combo doble")
        total += d*6
        order.append(d)
        t = order_validation("combo triple")
        total += t*7
        order.append(t)
        h = order_validation("helado McFlurby")
        total += h*2
        order.append(t)
        while True:
            ans = input("Confirma la transaccion? Y/N")
            if isinstance(ans, str) and (ans.capitalize == "Y" or ans.capitalize == "N"):
                break
            else:
                print("Respuesta incorrecta")
        if ans.capitalize == "Y":
            reg_client(name, order, total)
            print("\n")
            return total
        else: 
            return 0

def main():
    total = 0
    name = welcome()
    in_out_register(1, name, 0)
    while True:
        op = operation()
        if op == 1:
            total += load_order()
        elif op == 2:
            in_out_register(2, name,total)
            total = 0
            print("\n")
            name = welcome()
            in_out_register(1,name,0)
        else: 
            in_out_register(2, name,total)
            break
    print("Adios, tenga un buen dia!")
    system("pause")

main()