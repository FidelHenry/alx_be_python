class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"You have checked out: {book.title}")
                return
        print("Book not available or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"You have returned: {book.title}")
                return
        print("Book not found or was not checked out.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        else:
            print("Available Books:")
            for book in available:
                print(f"- {book.title} by {book.author}")
