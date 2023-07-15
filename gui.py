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


    # Pestaña "ESTUDIANTES"

    students_tab = ttk.Frame(notebook)
    students_table = Tables(students_tab)
    students_table.display_students_table()






    # Pestaña "PROFESORES"
    professors_tab = ttk.Frame(notebook)
    professors_table = Tables(professors_tab)
    professors_table.display_professors_table()



    # Pestaña "CURSOS"
    courses_tab = ttk.Frame(notebook)
    courses_table = Tables(courses_tab)
    courses_table.display_courses_table()
    
    
    
    # Pestaña "INSCRIPCIONES"
    inscriptions_tab = ttk.Frame(notebook)
    inscriptions_table = Tables(inscriptions_tab)
    inscriptions_table.display_inscriptions_table()





    notebook.add(students_tab, text='ESTUDIANTES')
    notebook.add(professors_tab, text='PROFESORES')
    notebook.add(courses_tab, text='CURSOS')
    notebook.add(inscriptions_tab, text='INSCRIPCIONES')

    notebook.pack(side='top')
    notebook.pack_propagate(False)

    window.mainloop()



  