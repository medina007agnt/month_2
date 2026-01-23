import sqlite3

def create_tables(connection):
    connection.execute('''
    CREATE TABLE students (
        student_name TEXT,
        age INTEGER,
        city TEXT
    )
    ''')
    conn.commit()
    conn.close()

def add_student(connection, student_name, age, city):
    connection.execute('''
    INSERT INTO students
    (student_name, age , city) VALUES
    (?, ?, ?)
    ''', (student_name, age , city))
    connection.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    create_tables(conn)

    add_student(conn, "Medina", "18", "Bishkek")