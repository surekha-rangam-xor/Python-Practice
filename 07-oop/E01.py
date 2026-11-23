 
class Book:
 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
 
    def describe(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"
 
    def read(self, count):
        self.current_page = min(self.current_page + count, self.pages)
 
    def progress(self):
        return round((self.current_page / self.pages) * 100, 1)
 
 
 
book = Book("Dune", "Frank Herbert", 412)
 
print(book.describe())
print(book.progress())
 
book.read(103)
print(book.current_page)
print(book.progress())
 
book.read(500)
print(book.current_page)
print(book.progress())
 