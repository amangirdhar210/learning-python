books_file= "utils/books_file.txt"

def _save_books_to_file(books):
    with open(books_file, "w") as books_data:
        for book in books:
            books_data.write(f"{book['title']},{book['author']},{int(book['pdh_li'])}\n")



def add_book(title, author):
    with open(books_file, "a") as books:
        books.write(f"{title},{author},0\n")


def get_all_books():
    book_list=[]
    with open(books_file, "r") as books:
        book_list= books.readlines()

    book_list=[book.strip().split(",") for book in book_list]
    return [
        {"title": book[0], "author": book[1], "pdh_li": book[2]}
        for book in book_list
    ]


def delete_book(name):
    books= get_all_books()
    books= [book for book in books if book['title']!= name]
    _save_books_to_file(books)
    

def mark_as_read(title):
    books= get_all_books()
    for book in books:
        if book["title"]== title:
            book["pdh_li"]= 1
            break
    _save_books_to_file(books)

