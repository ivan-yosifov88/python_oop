# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book

class Book:
    def __init__(self, name, content: str):
        self.name = name
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content + " and she love me"

class Printer:
    def get_book(self, book: Book, formatter: Formatter):
        return formatter.format(book)


bk = Book("I love BIBI", "How i love her")
print(Printer().get_book(bk, Formatter()))