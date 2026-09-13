from book import Book
from library import Library

# 1. Initialize our Library manager
my_library = Library()

# 2. Create some Book instances
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
book3 = Book("Dune", "Frank Herbert")

# 3. Add them to the library
my_library.add_link = ... # (or just use add_book)
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

print("\n--- Current Library Inventory ---")
my_library.list_books()

# 4. Search for a specific book and check it out
searched_book = my_library.find_book("1984")
if searched_book:
    print(f"\nFound: {searched_book.get_info()}")
    searched_book.check_out()

print("\n--- Updated Inventory Status ---")
my_library.list_books()