import utils
import tkinter
from tkinter import ttk

entry = ttk.Entry()

def imprimir_texto():
 print(entry.get())

# student = utils.Student(45075901, "Ivan", "Araolaza", "Sistemas", "ivanaraolaza@gmail.com", 10.00)

def main():
    # connection = utils.sqlite3.connect("INSTITUTO_JUAN_P_SEGADE.sqlite")      # Se conecta a la base de datos, y en caso de que no exista, la crea.
    # cursor = connection.cursor()                                        # Se genera el cursor para insertar las queries SQL.
    # if bool(utils.init(cursor, connection)):
    #     connection.close()
    #     print("Initialization succesful")
    
    # connection = utils.sqlite3.connect("INSTITUTO_JUAN_P_SEGADE.sqlite")
    # cursor = connection.cursor()

    # utils.System(cursor).add_student(student)
    # connection.commit()
    # connection.close()
        
    entry.place(x=10, y=10)
    boton = ttk.Button(text="Imprimir texto", command=imprimir_texto)
    boton.place(x=10, y=50)
    

if __name__ == '__main__':
    main()




