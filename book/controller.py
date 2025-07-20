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

def display_member_list_controller():
    display_member_bar()
    model.book_list()