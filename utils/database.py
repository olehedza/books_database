from .database_connection import DatabaseConnection
# import json
# import sqlite3


# books = []

# books_file = 'books.json'


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    # with open(books_file, 'w') as file:
    #     json.dump([], file)


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO books VALUES(?, ?, 0)", (name, author))

    # with open(books_file, 'a') as file:
    #     file.write(f'{name},{author},0\n')
    # books = get_all_books()
    # books.append({'name': name, 'author': author, 'read': False})
    # _save_all_books(books)


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')

        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]
    return books
    # with open(books_file, 'r') as file:
    #     # lines = [line.strip().split(',') for line in file.readlines()]
    #     return json.load(file)

    # books = [
    #     {'name': line[0], 'author': line[1], 'read': line[2]}
    #     for line in lines
    # ]
    #
    # return books


# def _save_all_books(books):
#     with open(books_file, 'w') as file:
#         json.dump(books, file)
    # for book in books:
    #     file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    # books = get_all_books()
    # for book in books:
    #     if book['name'] == name:
    #         book['read'] = True
    # _save_all_books(books)


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))

    # books = get_all_books()
    # books = [book for book in books if book['name'] != name]

    # _save_all_books(books)

    # def delete_book(name):
    #     for book in books:
    #         if book['name'] == name:
    #             books.remove(book)
