class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = True

class Library:
  def __init__(self):
    self._books = []
  
  def add_book(self,book):
    self._books.append(book)
  
  def check_out_book(self,title):
    for book in self._books:
      if book.title == title:
        if book._is_checked_out:
          return "{book.title} by {book.author}"
        else:
          return "is not available" 
    print(f"Book '{title}' not found in the library.")
    return False
  
  def return_book(self,title):
    for book in self._books:
      if book.title == title:
        return "{book.title} by {book.author}"
    print(f"Book '{title}' not found in the library.")
    return False
  
  def list_available_books(self):
    for book in self._books:
      print(f"{book.title} by {book.author}\n")







