from book import Book
from user import User
from author import Author

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
# Book Operations Menu
def book_operations():
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
                title = input("Enter book title: ")
                author_id = input("Enter author ID: ")
                isbn = input("Enter ISBN: ")
                pub_date = input("Enter publication date (YYYY-MM-DD): ")
                genre_id = input("Enter genre ID: ")
                book = Book(title, author_id, isbn, pub_date, genre_id)
                book.save_to_db()
            elif choice == "2":
                isbn = input("Enter ISBN of the book to borrow: ")
                Book.search_by_isbn(isbn).mark_borrowed()
            elif choice == "3":
                isbn = input("Enter ISBN of the book to return: ")
                Book.search_by_isbn(isbn).mark_returned()
            elif choice == "4":
                isbn = input("Enter ISBN to search: ")
                Book.search_by_isbn(isbn)
            elif choice == "5":
                Book.display_all_books()
            elif choice == "6":
                break
            else:
                print("Invalid choice, please try again.")

# User Operations Menu
def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(name, library_id)
            user.save_to_db() 
        elif choice == "2":
            library_id = input("Enter the library ID:")
            User.view_user_details(library_id)
        elif choice == "3":
            User.display_all_users()  
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

# Author Operations Menu
def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            author.save_to_db()
        elif choice == "2":
            author_id = input("Enter author ID: ")
            Author.view_author_details(author_id)
        elif choice == "3":
            Author.display_all_authors()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

# Run the system
if __name__ == "__main__":
    main_menu()

