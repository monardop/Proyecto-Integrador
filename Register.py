from datetime import datetime, date
import sqlite3

def current_datatime():
    """
    -Esta funcion retorna la fecha y hora para anexar al registro y a las ventas.
    -This function returns date and time to index into the sells and IN/OUT register.
    """
    message = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    return message

def in_out_register(op: int, name: str, total: float):
    todayDate = current_datatime()
    if op == 1:
        with open("registros.txt", "a") as f:
            f.write(f"IN {todayDate}; Encargad@: {name}")
        sql_register(1, [todayDate,name])
    elif op == 2:
        end_line = "#"
        with open("registros.txt", "a") as f:
            f.write(f"OUT {todayDate}; Encargad@: {name} ${total}")
            f.write(end_line*50)
        sql_register(2,[todayDate,name,total])
    
def register_client(name: str, order: list, total: float):
    todayDate = current_datatime()
    s, d, t, p = order
    with open("ventas.txt", "a") as f:
                f.write(f"{name}; {todayDate}; {s}; {d}; {t}; {p}; ${total}")
    sql_register(3,[name, todayDate, s, d, t, p, total])

def sql_register(op: int, args:list):
    conn = sqlite3.connect('comercio.sqlite')
    cursor = conn.cursor()
    if op== 1:
        date, name = args
        cursor.execute("INSERT INTO registro VALUES(?,?,?,?)",(name, date, 'IN', 0))
        conn.commit()
        conn.close()
    elif op == 2:
        date, name, total = args
        cursor.execute("INSERT INTO registro VALUES(?,?,?,?)",(name, date, 'OUT', total))
        conn.commit()
        conn.close()    
    elif op == 3:
        name,todayDate, s,d,t,p,total = args
        cursor.execute("INSERT INTO ventas VALUES(?,?,?,?,?,?,?)", (name,todayDate,s,d,t,p,total))
        conn.commit()
        conn.close()
