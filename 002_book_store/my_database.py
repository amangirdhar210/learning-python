books= []

def add_book(title, author):
    if {"title": title, "author":author, "pdh_li":False} in books:
        print("book already exists in store")
    try:
        books.append({"title": title, "author": author, "pdh_li": False})
    except Exception:
        print("some error occured! please check your code")
    else: 
        print(f"number of books in bookstore is {len(books)}")

    
def delete_book(name):
    for book in books:
        try:
            if book['title']==name:
                books.remove(book)
        except Exception:
            print("error occured while deleting a book")
        else:
            print(f"number of books in bookstore is {len(books)}")


def get_all_books():
    return books 


def mark_as_read(title):
    for book in books:
        if book["title"]== title:
            book["pdh_li"]= True
            break

