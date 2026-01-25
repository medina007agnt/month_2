import sqlite3


DB_NAME = "school_library.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)

    conn.commit()
    conn.close()
    print("Таблица books готова.")


def insert_books():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM books")

    cur.execute("""
    INSERT INTO books VALUES
    ('Clean Code', 'Robert Martin', 2008, 'Programming', 464, 3),
    ('Python Crash Course', 'Eric Matthes', 2016, 'Programming', 544, 5),
    ('Atomic Habits', 'James Clear', 2018, 'Self-help', 320, 6),
    ('Deep Work', 'Cal Newport', 2016, 'Productivity', 304, 4),
    ('Think and Grow Rich', 'Napoleon Hill', 1937, 'Business', 320, 2),
    ('The Alchemist', 'Paulo Coelho', 1988, 'Novel', 208, 7),
    ('Sapiens', 'Yuval Noah Harari', 2011, 'History', 498, 3),
    ('The Psychology of Money', 'Morgan Housel', 2020, 'Finance', 256, 5),
    ('The Subtle Art of Not Giving a F*ck', 'Mark Manson', 2016, 'Psychology', 224, 4),
    ('Rich Dad Poor Dad', 'Robert Kiyosaki', 1997, 'Finance', 336, 6)
    """)

    conn.commit()
    conn.close()
    print("Данные добавлены в таблицу.")


if __name__ == "__main__":
    create_table()
    insert_books()
