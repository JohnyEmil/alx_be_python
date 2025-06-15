class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return f"{book.title} by {book.author}"
                return "Book is not available"
        print(f"Book '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return f"{book.title} by {book.author}"
                return "Book was not checked out"
        print(f"Book '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        available_books = []
        for book in self._books:
            if not book._is_checked_out:
                available_books.append(f"{book.title} by {book.author}")
        return available_books







