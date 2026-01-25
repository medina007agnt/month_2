import sqlite3


def create_table():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        name_id INTEGER PRIMARY KEY AUTOINCREMENT,
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


# НОВЫЕ ФУНКЦИИ ПО ЗАДАНИЮ

def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE name_id = ?", (book_id,))
    conn.commit()
    conn.close()
    print(f"Книга с ID {book_id} удалена.")


def update_book_name(book_id, new_name):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET name = ? WHERE name_id = ?",
        (new_name, book_id)
    )
    conn.commit()
    conn.close()
    print(f"Книга с ID {book_id} переименована в '{new_name}'.")


def get_all_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books



if __name__ == "__main__":
    create_table()

    insert_books()

    delete_book(10)
    delete_book(13)
    delete_book(5)
    delete_book(15)

    update_book_name(2, "The White Ship (Updated)")

    print("\n--- Список всех книг в базе: ---")
    all_books = get_all_books()
    for book in all_books:
        print(book)
