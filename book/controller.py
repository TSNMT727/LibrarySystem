from book.view import (
    add_book as view_add_book,
    main_menu,
    user_input_main,
    user_continue,
    user_input_repeat,
    book_added_successfully,
    user_input_empty,
    user_input_invalid,
    b_attempts_maxed,
    balik_kampung,
    end_programm,
    display_member_bar
)
from book.model import BooksModel


def add_book_controller(book_model):
    max_attempts = 3
    counter = 0
    while True:
        book_id, book_title, book_author = view_add_book()
        if not book_id:
            user_input_empty()
            continue
        if book_model.book_exists(book_id):
            counter += 1
            if counter >= max_attempts:
                b_attempts_maxed()
                user_choice = user_continue()
                if user_choice == 'yes':
                    counter = 0
                    continue
                elif user_choice == 'no':
                    balik_kampung()
                    return
            else:
                user_input_repeat(max_attempts - counter)
                continue
        book_model.add_book(book_id, book_title, book_author)
        book_added_successfully()
        break

def display_member_list_controller(book_model):
    display_member_bar()
    book_model.book_list()

def main_menu_run():
    book_model = BooksModel()
    while True:
        main_menu()
        user_input = user_input_main()
        if not user_input:
            user_input_empty()
            continue
        if user_input == '1':
            add_book_controller(book_model)
        elif user_input == '2':
            display_member_list_controller(book_model)
        elif user_input == '3':
            end_programm()
            break
        else:
            user_input_invalid()