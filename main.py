import sqlite3


def init_db():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        cursor.executescript('''
        DROP TABLE IF EXISTS students;
        DROP TABLE IF EXISTS courses;    
        DROP TABLE IF EXISTS students_courses;
        PRAGMA foreign_keys = ON;
        
        CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            age INT,
            major VARCHAR
        
        );
        
        CREATE TABLE courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100)
        );
        
        CREATE TABLE students_courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        );
        ''')
        connection.commit()
        cursor.close()


def create_new_student(name, age, major):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, age, major)VALUES (?, ?, ?)",
                       [name, age, major])
        connection.commit()
        cursor.close()


def read_all_students():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        students = cursor.execute("SELECT * FROM students").fetchall()
        cursor.close()
    return students


def create_new_course(name):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO courses (name)VALUES (?)",
                       [name])
        connection.commit()
        cursor.close()


def read_all_courses():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        students = cursor.execute("SELECT * FROM courses").fetchall()
        cursor.close()
    return students


def main():
    while True:
        choice = int(input('''\nВведіть дію:
        1 - створити користувача
        2 - створити курс
        3 - прочитати всіх користувачів
        4 - прочитати всі курси
        0 - вийти
        \n'''))

        if choice == 1:
            name = input("ім'я\t")
            age = input("вік\t")
            major = input("спеціальність\t")
            create_new_student(name, age, major)

        if choice == 2:
            name = input("назва курсу:\t")
            create_new_course(name)

        elif choice == 3:
            for student in read_all_students():
                print(student)

        elif choice == 4:
            for course in read_all_courses():
                print(course)

        elif choice == 0:
            break


if __name__ == '__main__':
    init_db()
    main()
