def add_book():
    book_id = input("Input book's ID: ")
    book_title = input("Input book's title: ")
    book_author = input("Input book's author: ")
    return book_id, book_title, book_author


def user_input_main():
    user_input = input('Enter your choice: ').strip()
    return user_input


def user_continue():
    user_choice = input('Do you still want to continue(yes/no): ').strip().lower()
    return user_choice


def user_input_repeat(attempts_left):
    print(f'ID repeated. Please enter a brand new ID.({attempts_left} attempts left.)')

def display_member_bar():
    print(f'{"ID":<10}{"Title":<30}{"Author":<20}{"Status":<10}')
    print('-'*70)