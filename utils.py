import sqlite3

def init(cursor, connection) -> int:
    '''
    Si es la primera vez que se ejecuta el programa, se crean las tablas correspondientes. De lo contrario no se hace nada.
    '''
    error_code = 1
    try:
        cursor.execute("""
            CREATE TABLE estudiantes(
                dni UNSIGNED INT(8) NOT NULL PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                apellido VARCHAR(50) NOT NULL,
                especialidad VARCHAR(50) DEFAULT 'Ingresante',
                mail VARCHAR(70) NOT NULL,
                promedio UNSIGNED FLOAT(2,2))
        """)                                        # Se crea la tabla "estudiantes", con los registros correspondientes.

    except sqlite3.OperationalError as sqlite_error:
        print("No se pudo crear la tabla 'estudiantes'. Error: ", sqlite_error)
        error_code = 0
    
    try:
        cursor.execute("""
            CREATE TABLE profesores(
                dni UNSIGNED INT(8) NOT NULL PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                apellido VARCHAR(50) NOT NULL,
                mail VARCHAR(70) NOT NULL)
        """)                                        # Se crea la tabla "profesores", con los registros correspondientes.

    except sqlite3.OperationalError as sqlite_error:
        print("No se pudo crear la tabla 'profesores'. Error: ", sqlite_error)
        error_code = 0
    
    try:
        cursor.execute("""
            CREATE TABLE cursos(
                id_curso VARCHAR(6) NOT NULL PRIMARY KEY,
                asignatura VARCHAR(60) NOT NULL,
                id_profesor UNSIGNED INT(8),
                nivel UNSIGNED TINYINT(1) DEFAULT 0,
                FOREIGN KEY (id_profesor) REFERENCES profesores(dni))
        """)                                        # Se crea la tabla "cursos", con los registros correspondientes.

    except sqlite3.OperationalError as sqlite_error:
        print("No se pudo crear la tabla 'cursos'. Error: ", sqlite_error)
        error_code = 0

    try:
        cursor.execute("""
            CREATE TABLE inscripciones(
                id_inscripción INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                dni UNSIGNED INT(8) NOT NULL,
                id_curso VARCHAR(6) NOT NULL,
                nota UNSIGNED FLOAT(2,2) DEFAULT 0.00,
                FOREIGN KEY (dni) REFERENCES estudiantes(dni),
                FOREIGN KEY (id_curso) REFERENCES cursos(id_curso))
        """)                                        # Se crea la tabla "inscripciones", con los registros correspondientes.

    except sqlite3.OperationalError as sqlite_error:
        print("No se pudo crear la tabla 'inscripciones'. Error: ", sqlite_error)
        error_code = 0

    connection.commit()
    return error_code
    

class Student:
    def __init__(self, dni: int, name: str, lastname: str, email: str, career: str, average: float) -> None:
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.email = email
        self.career = career
        self.average = average


class Professor:
    def __init__(self, dni: int, name: str, lastname: str, email: str) -> None:
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.email = email


class Course:
    def __init__(self, course_id: int, subject: str, professor: Professor, level: str) -> None:
        self.course_id = course_id
        self.subject = subject
        self.professor = professor
        self.level = level


class Inscription:
    def __init__(self, inscription_id: int, student: Student, course: Course ) -> None:
        self.inscription_id = inscription_id
        self.student = student.dni
        self.course = course.course_id


class System:
    def __init__(self, cursor) -> None:
        self.cursor = cursor

    
    def add_student(self, student: Student):
        self.cursor.execute(
            "INSERT INTO estudiantes VALUES(?,?,?,?,?,?)",
            (student.dni, student.name, student.lastname, student.email, student.career, student.average)
        )
    

    def add_professor(self, professor: Professor ):
        self.cursor.execute(
            "INSERT INTO profesores VALUES(?,?,?,?)",
            (professor.dni, professor.name, professor.lastname, professor.email)
        )

    
    def create_new_course(self, course: Course):
        self.cursor.execute(
            "INSERT INTO cursos VALUES(?,?,?,?)",
            (course.course_id, course.subject, course.professor.dni, course.level)
        )


    def assign_course(self, course: Course, professor: Professor):
        self.cursor.execute(
            "UPDATE cursos SET dni = ? WHERE id_curso = ?",
            (professor.dni, course.course_id)
        )
        

    def new_inscription(self, student: Student, course: Course, inscription: Inscription):
        self.cursor.execute(
            "INSERT INTO inscripciones VALUES(dni=?,id_curso=?)",
            (student.dni, course.course_id )
        )

        inscription.inscription_id = self.cursor.execute(
            "SELECT id_inscripcion FROM inscripciones WHERE dni=?",
            (student.dni)
        )

     