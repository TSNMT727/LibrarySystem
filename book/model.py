from utils.constants import BOOKS_FILE

def all_books():
    books = []
    try:
        with open(BOOKS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    books.append({
                        'id': parts[0],
                        'title': parts[1],
                        'author': parts[2],
                        'is_available': parts[3] == 'True'
                    })
    except FileNotFoundError:
        open(BOOKS_FILE, 'w').close()

    return books

def get_book(book_id):
    books = all_books()
    for book in books:
        if book['id'] == book_id:
            return book
    return None

def add_book(book_id, title, author):
    with open(BOOKS_FILE, 'a') as f:
        f.write(f'{book_id},{title},{author},{True}\n')
    return True


def update_book_availability(_book_id: str, _availability: bool):
    books = all_books()
    updated = []
    for book in books:
        if book["id"] == _book_id:
            updated.append(convert_to_book_str({**book, "is_available": _availability }))
        else:
            updated.append(convert_to_book_str(book))

    with open(BOOKS_FILE, "w") as file:
        for line in updated:
            file.write(line)


def convert_to_book_str(dict):
    return f"{dict['id']},{dict['title']},{dict['author']},{dict['is_available']}\n"