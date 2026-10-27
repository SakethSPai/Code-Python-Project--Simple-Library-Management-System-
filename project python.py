class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!")

    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        print("\n--- Book List ---")

        for book in self.books:
            status = "Available" if book.available else "Issued"

            print("ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)
            print("----------------")

    def search_book(self):
        title = input("Enter book title to search: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found!")
                print("ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                return

        print("Book not found.")

    def issue_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")

                return

        print("Book not found.")

    def delete_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book deleted successfully.")
                return

        print("Book not found.")


library = Library()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")