import sqlite3

def init_db():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        cursor.executescript('''
        DROP TABLE IF EXISTS students;
        DROP TABLE IF EXISTS courses;    
        
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
        
        ''')
        connection.commit()
        cursor.close()


if __name__ == '__main__':
    init_db()
