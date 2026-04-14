class Library:

    # Constructor to initialize book details
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    # Method to checkout a book
    def checkout_book(self):
        if self.available:
            print(self.book_name, "has been checked out.")
            self.available = False
        else:
            print(self.book_name, "is not available.")

    # Method to display book details
    def display_books(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"

        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)
       


# Creating objects for different books
book1 = Library("A Christmas Carol", "Charles Dickens")
book2 = Library("harry potter", "j.k rowling")
book3 = Library("Computer Networks", "Andrew Tanenbaum")

# Display books
book1.display_books()
book2.display_books()
book3.display_books()

# Checkout a book
book1.checkout_book()

# Display again to see updated availability
book1.display_books()   