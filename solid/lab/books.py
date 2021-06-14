class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.books_titles = set()

    @staticmethod
    def is_book_in_books(book, books):
        return book in books

    def add_book(self, book):
        if not self.is_book_in_books(book, self.books):
            self.books.append(book)
            self.books_titles.add(book.title)

    def find_book(self, title):
        if self.is_book_in_books(title, self.books_titles):
            return book.title


book = Book("bibi poems", "bibi")
library = Library("The Best")

library.add_book(book)
print(library.find_book("bibi poems"))