from book.view import (
    add_book as view_add_book,
    user_continue,
    user_input_repeat,
    display_member_bar
)
import book.model as model
# from book.model import BooksModel


def add_book_controller():
    max_attempts = 3
    counter = 0
    while True:
        book_id, book_title, book_author = view_add_book()
        if not book_id:
            print("Please enter somehting bro.")
            continue
        if model.book_exists(book_id):
            counter += 1
            if counter >= max_attempts:
                print("You have reached max attempts.")
                user_choice = user_continue()
                if user_choice == 'yes':
                    counter = 0
                    continue
                elif user_choice == 'no':
                    print("Returning to main menu...")
                    return
            else:
                user_input_repeat(max_attempts - counter)
                continue
        model.add_book(book_id, book_title, book_author)
        print("Book added sucessfully")
        break

def handle_get_book(book_id):
    book = model.get_book(book_id)
    if book:
        # Add 'id' and 'available' fields for lending_service compatibility
        book_with_status = book.copy()
        book_with_status['id'] = book['bookid']
        book_with_status['available'] = (book['bookstatus'] == 'available')
        return book_with_status
    else:
        return None

# Helper to update book status in file
def _update_book_status(book_id, new_status):
    books = model.all_books()
    updated = False
    for book in books:
        if book['bookid'] == book_id:
            book['bookstatus'] = new_status
            updated = True
    if updated:
        # Write all books back to file
        with open(model.BOOKS_FILE, 'w') as f:
            for book in books:
                f.write(f"{book['bookid']},{book['booktitle']},{book['bookauthor']},{book['bookstatus']}\n")
    return updated

def handle_mark_book_unavailable(book_id):
    print(f"Book {book_id} marked as unavailable.")


def handle_mark_book_available(book_id):
    print(f"Book {book_id} marked as available.")


def display_member_list_controller():
    display_member_bar()
    model.book_list()