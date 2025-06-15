class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self) -> bool:
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self) -> bool:
        """Return the book if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return str(book)
                return "Book is not available"
        print(f"Book '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return str(book)
                return "Book was not checked out"
        print(f"Book '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        available_books = []
        for book in self._books:
            if not book._is_checked_out:
                available_books.append(f"{book.title} by {book.author}")
        return available_books







