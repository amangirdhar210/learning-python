import my_database

WELCOME_TEXT= """Welcome to the Book Store!
Here we provide all kinds of books just tell us how can we help you!
"""

MENU_TEXT="""
Enter 'a' to add a book
Enter 'l' to list all books
Enter 'd' to delete a book
Enter 'r' to read a book
Enter 'q' to exit the bookstore
"""



def add_book():
    title= input("Please enter the title of the new book: ")
    author= input("Please enter the author of the new book: ")
    my_database.add_book(title, author)


def list_all_books():
    books= my_database.get_all_books()
    if len(books)!= 0:
        for book in books:
            print(book)
    else:
        print("no books in the store! sorry")

def delete_book():
    title= input("please enter the title of the book to delete: ")
    my_database.delete_book(title)

def read_book():
    title= input("Please enter the book you want to read: ")
    my_database.mark_as_read(title)

method_set= {
    "a": add_book,
    "l": list_all_books,
    "d": delete_book,
    "r": read_book
}

def menu():
    print(WELCOME_TEXT)
    print(MENU_TEXT)
    user_input= input("Please enter your choice: ")
    while user_input != 'q':
        try:
            method_set[user_input]()
        except:
            print("please enter a valid input")
        print(MENU_TEXT)
        user_input= input("please enter your choice: ")
    


menu()
