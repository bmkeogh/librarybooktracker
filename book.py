class Book:
    # 1. The Constructor: Initializes a new Book object
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False  # Default state when bought/added

    # 2. A Method to check out the book
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out!")

    # 3. A Method to return the book
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned to the library.")
        else:
            print(f"'{self.title}' was not checked out.")

   # 4. A method to show info about the book
    def get_info(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"Title: '{self.title}' by {self.author} | Status: {status}"