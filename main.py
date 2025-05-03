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


if __name__ == '__main__':
    init_db()
