import sqlite3


# CRUD - create, read(select) update, delete

def create_tables(connection):
    connection.execute('''DROP TABLE IF EXISTS students''')
    connection.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        age INTEGER,
        city TEXT 
    )
    ''')


def add_student(connection, student_name, age, city):
    connection.execute('''
    INSERT INTO students
    (student_name, age, city) VALUES 
    (?, ?, ?)
    ''', (student_name, age, city))
    connection.commit()


def delete_student(connection, student_id):
    connection.execute(
        'DELETE FROM students WHERE student_id = ?',
        (student_id,)
    )
    connection.commit()


def delete_student_by_name(connection, student_name):
    connection.execute(
        "DELETE FROM students WHERE student_name = ?",
        (student_name,)
    )
    connection.commit()


def get_all_students(connection):
    result = connection.execute(
        "SELECT student_id, student_name FROM students"
    )
    return result.fetchall()


def get_student(connection, student_id):
    result = connection.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )
    return result.fetchone()


def change_student(connection, student_id, new_name, new_age, new_city, ):
    connection.execute(
        """
        UPDATE students
        SET student_name = ?, age = ?, city = ?
        WHERE student_id = ?
        """,
        (new_name, new_age, new_city, student_id)
    )
    connection.commit()

    conn = sqlite3.connect("database.db")
    create_tables(conn)

    add_student(conn, "Данил", 18, "Бишкек")
    add_student(conn, "Данил", 18, "Кара-Балта")
    add_student(conn, "Аян", 20, "Бишкек")
    add_student(conn, "Игорь", 18, "Каракол")
    delete_student(conn, 1)

    for st in get_all_students(conn):
        print(st)

    print(get_student(conn, 3))
    print("*********")
    change_student(conn, 4, "Егор", 18, "Бишкек")
    for st in get_all_students(conn):
        print(st)


