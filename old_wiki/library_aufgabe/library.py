class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\n")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_books = []

    def display_info(self):
        print(f"Name: {self.name}\nMember ID: {self.member_id}\n")

    def check_out_book(self, book):
        if not book.checked_out:
            book.checked_out = True
            self.checked_out_books.append(book)
            print(f"{self.name} checked out {book.title}")
        else:
            print(f"Sorry, {book.title} is already checked out.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.checked_out = False
            self.checked_out_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not have {book.title} checked out.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_info()

    def display_members(self):
        print("Library Members:")
        for member in self.members:
            member.display_info()


# Example usage:
# Create books, members, and library
book1 = Book("The Python Bible", "John C. Python", "123456789")
book2 = Book("Data Science for Beginners", "Alice Data", "987654321")

member1 = Member("Bob", "M001")
member2 = Member("Alice", "M002")

library = Library()

# Add books and members to the library
library.add_book(book1)
library.add_book(book2)

library.add_member(member1)
library.add_member(member2)

# Display library information
library.display_books()
library.display_members()

# Perform check-out and return operations
member1.check_out_book(book1)
member2.check_out_book(book1)  # Should print that the book is already checked out
member2.return_book(book2)     # Should print that the book was not checked out by member2

# Display library information after operations
library.display_books()
library.display_members()
