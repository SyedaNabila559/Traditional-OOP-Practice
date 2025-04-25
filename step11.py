# 11. Class Methods

# Assignment:

# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_books = 0  # Class variable to track total number of books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"📚 Total books updated: {cls.total_books}")

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment total books when a new book is added

# --- Testing the Book class ---
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Display total number of books
print(f"📘 Total books in library: {Book.total_books}")

