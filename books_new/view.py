def add_book():
    book_id = input("Input book's ID: ")
    book_title = input("Input book's title: ")
    book_author = input("Input book's author: ")
    return book_id, book_title, book_author


def main_menu():
    print('choose 1-7')
    print('Add books = 1')
    print('Display books = 2')
    print('exit = 3')


def user_input_main():
    user_input = input('Enter your choice: ').strip()
    return user_input


def user_continue():
    user_choice = input('Do you still want to continue(yes/no): ').strip().lower()
    return user_choice


def user_input_repeat(attempts_left):
    print(f'ID repeated. Please enter a brand new ID.({attempts_left} attempts left.)')


def book_added_successfully():
    print("Book added sucessfully")


def user_input_empty():
    print("Please enter somehting bro.")


def user_input_invalid():
    print('Invalid input, please try again.')


def b_id_repeat():
    print('Book ID repeated.')


def b_attempts_maxed():
    print("You have reached max attempts.")


def balik_kampung():
    print("Returning to main menu...")


def end_programm():
    print("Ending the program...")


def display_member_bar():
    print(f'{"ID":<10}{"Title":<30}{"Author":<20}{"Status":<10}')
    print('-'*70)