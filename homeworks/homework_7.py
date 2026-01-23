import sqlite3


def create_table():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()


    cursor.execute("""
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
    print("Таблица books создана или уже существует.")


def insert_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    books = [
        ("White Steamship", "Chyngyz Aitmatov", 1970, "Story", 336, 5),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 320, 10),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7),
        ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 4),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Drama", 281, 6),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 3),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 1),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological", 671, 4),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fairy tale", 96, 8)
    ]

    cursor.executemany("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()
    print("Книги добавлены в таблицу.")


if __name__ == "__main__":
    create_table()
    insert_books()
