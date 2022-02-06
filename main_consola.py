from os import system
import Register as reg

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
            reg.register_client(name, order, total)
            print("\n")
            return total
        else: 
            return 0

def main():
    total = 0
    name = welcome()
    reg.in_out_register(1, name, 0)
    while True:
        op = operation()
        if op == 1:
            total += load_order()
        elif op == 2:
            reg.in_out_register(2, name,total)
            total = 0
            print("\n")
            name = welcome()
            reg.in_out_register(1,name,0)
        else: 
            reg.in_out_register(2, name,total)
            break
    print("Adios, tenga un buen dia!")
    system("pause")

if __name__ == '__main__':
    main()