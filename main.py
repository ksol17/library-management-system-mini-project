from book import Book
from user import User
from author import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.book_operations()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.author_operations()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    # Book Operations Menu
    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Select an option (1-6): ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.display_all_books()
            elif choice == "6":
                break
            else:
                print("Invalid choice, please try again.")

    # Book Methods
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        pub_date = input("Enter publication date (YYYY-MM-DD): ")
        book = Book(title, author, genre, pub_date)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        user_id = input("Enter user library ID: ")
        book_title = input("Enter book title to borrow: ")

        user = self.find_user_by_id(user_id)
        book = self.find_book_by_title(book_title)

        if user and book:
            if book.is_available():
                user.borrow_book(book.get_title())
                book.set_availability(False)
                print(f"Book '{book_title}' borrowed successfully.")
            else:
                print(f"Book '{book_title}' is currently unavailable.")
        else:
            print("User or book not found.")

    def return_book(self):
        user_id = input("Enter user library ID: ")
        book_title = input("Enter book title to return: ")

        user = self.find_user_by_id(user_id)
        book = self.find_book_by_title(book_title)

        if user and book:
            user.return_book(book.get_title())
            book.set_availability(True)
            print(f"Book '{book_title}' returned successfully.")
        else:
            print("User or book not found.")

    def search_book(self):
        book_title = input("Enter book title to search: ")
        book = self.find_book_by_title(book_title)

        if book:
            print("Book found:")
            print(book.display_book_info())
        else:
            print("Book not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nAll Books:")
            for book in self.books:
                print(book.display_book_info())

    # User Operations Menu
    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.view_user_details()
            elif choice == "3":
                self.display_all_users()
            elif choice == "4":
                break
            else:
                print("Invalid choice, please try again.")

    # User Methods
    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        user = User(name, library_id)
        self.users.append(user)
        print(f"User '{name}' added successfully.")

    def view_user_details(self):
        library_id = input("Enter library ID: ")
        user = self.find_user_by_id(library_id)

        if user:
            print(user.display_user_info())
        else:
            print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users found.")
        else:
            print("\nAll Users:")
            for user in self.users:
                print(user.display_user_info())

    # Author Operations Menu
    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.add_author()
            elif choice == "2":
                self.view_author_details()
            elif choice == "3":
                self.display_all_authors()
            elif choice == "4":
                break
            else:
                print("Invalid choice, please try again.")

    # Author Methods
    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        author = Author(name, biography)
        self.authors.append(author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter author name: ")
        author = self.find_author_by_name(name)

        if author:
            print(author.display_author_info())
        else:
            print("Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors found.")
        else:
            print("\nAll Authors:")
            for author in self.authors:
                print(author.display_author_info())

    # Helper Methods
    def find_user_by_id(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None

    def find_book_by_title(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None

    def find_author_by_name(self, name):
        for author in self.authors:
            if author.get_name() == name:
                return author
        return None

# Run the program
if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.main_menu()

