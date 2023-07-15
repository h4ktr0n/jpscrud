import utils
import gui
from gui import tk
from gui import ttk



# student = utils.Student(45075901, "Ivan", "Araolaza", "Sistemas", "ivanaraolaza@gmail.com", 10.00)


def main():
    gui.run_gui()
    
    # main_label = ttk.Label(window, text="INSTITUTO JUAN P SEGADE")
    # main_label.pack(side= 'top')
    # gui.home_frame(window)
    # gui.options_frame(window)


    connection = utils.sqlite3.connect("INSTITUTO_JUAN_P_SEGADE.sqlite")      # Se conecta a la base de datos, y en caso de que no exista, la crea.
    cursor = connection.cursor()                                        # Se genera el cursor para insertar las queries SQL.
    if bool(utils.init(cursor, connection)):
        connection.close()
        print("Initialization succesful")
    

if __name__ == '__main__':
    main()




