class Library:
    def __init__(self):
        # The library starts with an empty list to hold Book objects
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
            return

        for book in self.books:
            print(book.get_info())

    def find_book(self, title):
        # Search through our collection for a matching title (case-insensitive)
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None  # Return None if the book isn't found