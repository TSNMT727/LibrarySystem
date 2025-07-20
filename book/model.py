import os
import textwrap

BOOKS_FILE = 'LibrarySystem/data/books.txt'

def file_exist():
    f = open(BOOKS_FILE, "a")

def all_books():
    books = []
    with open(BOOKS_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                books.append({
                    'bookid': parts[0],
                    'booktitle': parts[1],
                    'bookauthor': parts[2],
                    'bookstatus': parts[3]
                })
    return books

def book_exists(book_id):
    books = all_books()
    return any(book['bookid'] == book_id for book in books)

def add_book(book_id, booktitle, bookauthor):
    with open(BOOKS_FILE, 'a') as f:
        f.write(f'{book_id},{booktitle},{bookauthor},available\n')
    return True

def book_list():
    with open(BOOKS_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            titles = textwrap.wrap(parts[1], width=29)
            authors = textwrap.wrap(parts[2], width=19)
            max_lines = max(len(titles), len(authors))
            titles += [''] * (max_lines - len(titles))
            authors += [''] * (max_lines - len(authors))
            for i in range(max_lines):
                if i == 0:
                    print(f'{parts[0]:<10}{titles[i]:<30}{authors[i]:<20}{parts[3]:<10}')
                else:
                    print(f'{"":<10}{titles[i]:<30}{authors[i]:<20}{"":<10}')

# Initialize file
file_exist()
