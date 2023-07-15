import utils
import tkinter as tk
import ttkbootstrap as ttk


class Tables():

    def __init__(self, parent) -> None:
        self.students_table = ttk.Treeview(parent, columns=('dni', 'name', 'lastname', 'email', 'career', 'average'), show= 'headings')
        self.professors_table = ttk.Treeview(parent, columns=('dni', 'name', 'lastname', 'email'), show= 'headings')
        self.courses_table = ttk.Treeview(parent, columns=('course_id', 'subject', 'professor', 'level'), show= 'headings')
        self.inscriptions_table = ttk.Treeview(parent, columns=('inscription_id', 'student', 'course'), show= 'headings')


    def display_students_table(self):
        self.students_table.heading('dni', text='DNI')
        self.students_table.heading('name', text='Nombre')
        self.students_table.heading('lastname', text='Apellido')
        self.students_table.heading('email', text='Mail')
        self.students_table.heading('career', text='Especialidad')
        self.students_table.heading('average', text='Promedio')
        self.students_table.pack(fill='both',expand=True)


    def display_professors_table(self):
        self.professors_table.heading('dni', text='DNI')
        self.professors_table.heading('name', text='Nombre')
        self.professors_table.heading('lastname', text='Apellido')
        self.professors_table.heading('email', text='Mail')
        self.professors_table.pack(fill='both',expand=True)


    def display_courses_table(self):
        self.courses_table.heading('course_id', text='ID')
        self.courses_table.heading('subject', text='Materia')
        self.courses_table.heading('professor', text='Profesor')
        self.courses_table.heading('level', text='Nivel/Año')
        self.courses_table.pack(fill='both',expand=True)


    def display_inscriptions_table(self):
        self.inscriptions_table.heading('inscription_id', text='N° de Inscripción')
        self.inscriptions_table.heading('student', text='Estudiante')
        self.inscriptions_table.heading('course', text='Curso')
        self.inscriptions_table.pack(fill='both',expand=True)  


def run_gui():

    # Creación de la ventana principal.
    window = ttk.Window()
    window.title("Instituto Juan P. Segade")
    window.geometry('800x600')

    notebook = ttk.Notebook(window)


    #* ---------------------------------- Pestaña "ESTUDIANTES" ------------------------------------------------

    # Creación de tabs relacionadas con el menú de "estudiantes"
    students_tab = ttk.Frame(notebook)
    students_menu = ttk.Notebook(students_tab)

    # Se muestra una tabla con los registros cargados en la base de datos.  Esto corresponde a la operación de visualización.
    students_table = Tables(students_tab)
    students_table.display_students_table()

    # Creación de las pestañas de las otras operaciones CRUD.
    add_student = ttk.Frame(students_menu)
    remove_student = ttk.Frame(students_menu)
    update_student = ttk.Frame(students_menu)
    
    # Pestaña "Agregar estudiante"
    dni_entry = ttk.Entry(add_student)
    name_entry = ttk.Entry(add_student)
    last_name_entry = ttk.Entry(add_student)
    email_entry = ttk.Entry(add_student)
    career_entry = ttk.Entry(add_student)
    average_entry = ttk.Entry(add_student)

    add_button = ttk.Button(add_student, text="AGREGAR ESTUDIANTE")

    dni_entry.pack()
    name_entry.pack()
    last_name_entry.pack()
    email_entry.pack()
    career_entry.pack()
    average_entry.pack()

    add_button.pack()


    # Pestaña "Eliminar estudiante"
    dni_label = ttk.Label(remove_student, text="Buscar por DNI:")
    dni_to_remove_entry = ttk.Entry(remove_student)

    dni_label.pack()
    dni_to_remove_entry.pack()


    # Pestaña "Actualizar información"

    new_dni_entry = ttk.Entry(update_student)
    new_name_entry = ttk.Entry(update_student)
    new_last_name_entry = ttk.Entry(update_student)
    new_email_entry = ttk.Entry(update_student)
    new_career_entry = ttk.Entry(update_student)
    new_average_entry = ttk.Entry(update_student)

    update_button = ttk.Button(update_student, text="ACTUALIZAR")

    new_dni_entry.pack()
    new_name_entry.pack()
    new_last_name_entry.pack()
    new_email_entry.pack()
    new_career_entry.pack()
    new_average_entry.pack()

    update_button.pack()


    # Se agregan los menúes a la pestaña
    students_menu.add(add_student, text='Agregar Estudiante')
    students_menu.add(remove_student, text='Eliminar Estudiante')
    students_menu.add(update_student, text='Actualizar Información')
    students_menu.pack(side='left')
    notebook.add(students_tab, text='ESTUDIANTES')

    #* --------------------------------------------------------------------------------------------------------


    ###########################################################################################################


    #* ---------------------------------- Pestaña "PROFESORES" --------------------------------------------------

    # Creación de tabs relacionadas con el menú de "profesores"
    professors_tab = ttk.Frame(notebook)
    professors_menu = ttk.Notebook(professors_tab)

    # Se muestra una tabla con los registros cargados en la base de datos.  Esto corresponde a la operación de visualización.
    professors_table = Tables(professors_tab)
    professors_table.display_professors_table()

    # Creación de las pestañas de las otras operaciones CRUD.
    add_professor = ttk.Frame(professors_menu)
    remove_professor = ttk.Frame(professors_menu)
    update_professor = ttk.Frame(professors_menu)
    
    # Pestaña "Agregar profesor"
    dni_entry = ttk.Entry(add_professor)
    name_entry = ttk.Entry(add_professor)
    last_name_entry = ttk.Entry(add_professor)
    email_entry = ttk.Entry(add_professor)

    add_button = ttk.Button(add_professor, text="AGREGAR PROFESOR")

    dni_entry.pack()
    name_entry.pack()
    last_name_entry.pack()
    email_entry.pack()

    add_button.pack()


    # Pestaña "Eliminar profesor"
    dni_label = ttk.Label(remove_professor, text="Buscar por DNI:")
    dni_to_remove_entry = ttk.Entry(remove_professor)

    dni_label.pack()
    dni_to_remove_entry.pack()


    # Pestaña "Actualizar información"

    new_dni_entry = ttk.Entry(update_professor)
    new_name_entry = ttk.Entry(update_professor)
    new_last_name_entry = ttk.Entry(update_professor)
    new_email_entry = ttk.Entry(update_professor)
    new_career_entry = ttk.Entry(update_professor)
    new_average_entry = ttk.Entry(update_professor)

    update_button = ttk.Button(update_professor, text="ACTUALIZAR")

    new_dni_entry.pack()
    new_name_entry.pack()
    new_last_name_entry.pack()
    new_email_entry.pack()
    new_career_entry.pack()
    new_average_entry.pack()

    update_button.pack()


    # Se agregan los menúes a la pestaña
    professors_menu.add(add_professor, text='Agregar profesor')
    professors_menu.add(remove_professor, text='Eliminar profesor')
    professors_menu.add(update_professor, text='Actualizar Información')
    professors_menu.pack(side='left')
    notebook.add(professors_tab, text='PROFESORES')

    #* --------------------------------------------------------------------------------------------------------

    ###########################################################################################################

    #* ------------------------------------ Pestaña "CURSOS" --------------------------------------------------

    courses_tab = ttk.Frame(notebook)
    courses_table = Tables(courses_tab)
    courses_table.display_courses_table()
    notebook.add(courses_tab, text='CURSOS')
    #* --------------------------------------------------------------------------------------------------------

    ###########################################################################################################
    
    #* ---------------------------------------- Pestaña "INSCRIPCIONES" ---------------------------------------

    inscriptions_tab = ttk.Frame(notebook)
    inscriptions_table = Tables(inscriptions_tab)
    inscriptions_table.display_inscriptions_table()
    notebook.add(inscriptions_tab, text='INSCRIPCIONES')

    #* --------------------------------------------------------------------------------------------------------

    ###########################################################################################################
    notebook.pack(side='top')
    notebook.pack_propagate(False)

    window.mainloop()



  