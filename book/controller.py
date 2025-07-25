import book.model as model

import utils.helpers as h
from utils.constants import MAX_ATTEMPTS

from tabulate import tabulate

def handle_books_exist():
    books = model.all_books()
    if not books:
        return False
    return True

def handle_add_book():
    counter = 0
    adding = True

    while adding:
        while counter < MAX_ATTEMPTS:
            # Get user input for book id
            book_id = input("\nEnter book ID: ")
            
            # If book ID already exists, increment counter and prompt again
            if model.get_book(book_id):
                print("Book ID already exists. Please enter a new ID.")
                counter += 1
                continue

            # If book ID is unique, get title and author and add the book
            else:
                title = input("Enter book title: ")
                author = input("Enter book author: ")

                model.add_book(book_id, title, author)
                print("Book added successfully.")
                adding = False
                break
        else:
            if not h.handle_max_attempts():
                break
            counter = 0
            continue

        to_continue = h.handle_continue()
        if to_continue:
            counter = 0
            adding = True

def handle_get_book(_book_id: str):
    return model.get_book(_book_id)

def handle_mark_book_unavailable(_book_id: str):
    model.update_book_availability(_book_id, False)
    print("Book availability updated")

def handle_mark_book_available(_book_id: str):
    model.update_book_availability(_book_id, True)
    print("Book availability updated")

def handle_list_books():
    books = model.all_books()
    if len(books) == 0:
        print("No books found")
    else:
        rows = []
        for book in books:
            row = []
            for key in book.keys():
                row.append(book[key])
            rows.append(row)

            # print(book)

        headers = [key.upper() for key in books[0].keys()]
        print("\n" + tabulate(rows, headers, tablefmt="rounded_grid"))