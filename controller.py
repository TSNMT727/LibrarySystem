from view import LibraryView
from model import BooksModel

class LibraryController():
    def __init__(self):
        self.view = LibraryView()
        self.book_model = BooksModel()

    def add_book(self):
        max = 3
        counter = 0

        while True:
            book_id, book_title, book_author = self.view.add_book()

            if not book_id:
                self.view.user_input_empty()
                continue
            if self.book_model.book_exists(book_id):
                counter += 1
                if counter >= max:
                    self.view.b_attempts_maxed()
                    user_choice = self.view.user_continue()
                    if user_choice == 'yes':
                        counter = 0
                        continue
                    elif user_choice == 'no':
                        self.view.balik_kampung()
                        return
                else:
                    self.view.user_input_repeat(max - counter)
                    continue
            self.book_model.add_book(book_id, book_title, book_author)
            self.view.book_added_successfully()
            break

    def display_member_list(self):
        self.view.display_member_bar()
        self.book_model.book_list()


    def main_menu_run(self):
        while True:
            self.view.main_menu()
            user_input = self.view.user_input_main()

            if not user_input:
                self.view.user_input_empty()
            if user_input == '1':
                LibraryController.add_book(self)
            elif user_input == '2':
                LibraryController.display_member_list(self)
            elif user_input == '3':
                self.view.end_programm()
                break
            else:
                self.view.user_input_invalid