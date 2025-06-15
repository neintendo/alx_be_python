class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # private attribute

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Library:
    def __init__(self):
        self._books = []  # private list of books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print("No available copy of '{}' to check out.".format(title))

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print("No checked out copy of '{}' to return.".format(title))

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(book)
