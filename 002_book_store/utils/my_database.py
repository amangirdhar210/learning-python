import sqlite3

def create_table():
    connection= sqlite3.connect("data.db")
    cursor= connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(title text PRIMARY KEY, author text, pdh_li integer)')
    connection.commit()
    connection.close()


def add_book(title, author):
    connection= sqlite3.connect("data.db")
    cursor= connection.cursor()
    
    cursor.execute("INSERT INTO books VALUES(?,?,0)", (title, author))
    
    
    connection.commit()
    connection.close()


def get_all_books():
    books=[]
    connection= sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('Select * from books')
    rows= cursor.fetchall()
    connection.close()
    for row in rows:
        books.append({"title": row[0], "author": row[1], "pdh_li":row[2]})
    return books

def delete_book(name):
    connection= sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute('DELETE FROM books where title=?', (name,))
    connection.commit()
    connection.close()
    

def mark_as_read(title):
    connection= sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('UPDATE books SET pdh_li=1 where title=?', (title,))

