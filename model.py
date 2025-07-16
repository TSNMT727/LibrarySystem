import os
import textwrap

class BooksModel:
    def __init__(self, filename = 'books.txt'):
        self.filename = filename
        self.file_exist()
        
    def file_exist(self):
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

    def all_books(self):
        books = []
        with open(self.filename, 'r') as f:
            for lines in f:
                parts = lines.strip().split(',')
                if len(parts) >= 4:
                    books.append({
                        'bookid': parts[0],
                        'booktitle': parts[1],
                        'bookauthor': parts[2],
                        'bookstatus': parts[3]
                    })
        return books

    def book_exists(self, book_id):
        books = self.all_books()
        return any(book['bookid']== book_id for book in books)
    
    def add_book(self, book_id, booktitle, bookauthor):
        bookstatus = "available"
        with open(self.filename, 'a') as add:
            add.write(f'{book_id},{booktitle},{bookauthor},{bookstatus}\n')
        return True
    
    def book_list(self):
        with open(self.filename, 'r') as f:
            for line in f:
                part = line.strip().split(',')
                #avoid crossing the line
                titles = textwrap.wrap(part[1], width=29)
                authors = textwrap.wrap(part[2], width=19)
                max_lines= max(len(titles), len(authors))
                titles += [''] * (max_lines - len(titles))
                authors += [''] * (max_lines - len(authors))
                for i in range(max_lines):
                    if i == 0:
                        print(f'{part[0]:<10}{titles[i]:<30}{authors[i]:<20}{part[3]:<10}')
                    else:
                        print(f'{'':<10}{titles[i]:<30}{authors[i]:<20}{'':<10}')
        