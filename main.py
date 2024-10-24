import re
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

            try: 

                if choice == "1":
                    isbn = input("Enter ISBN: ")
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    genre = input("Enter genre: ")
                    pub_date = input("Enter publication date (YYYY-MM-DD): ")
                    # Validate date format
                    if not re.match(r"\d{4}-\d{2}-\d{2}", pub_date):
                        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
                
                    book = Book(isbn, title, author, genre, pub_date)
                    book.save_to_db()
                    print("Book added successfully.")
                elif choice == "2":
                    isbn = input("Enter ISBN of the book to borrow: ")
                    Book.search_by_isbn(isbn)
                    if book:
                        book.mark_borrowed()

                elif choice == "3":
                    isbn = input("Enter ISBN of the book to return: ")
                    Book.search_by_isbn(isbn)
                    if book:
                        book.mark_borrowed()

                elif choice == "4":
                    isbn = input("Enter ISBN to search: ")
                    Book.search_by_isbn(isbn)
                    if book:
                        print(f"Book Found: {book._title}, Author: {book._author}, Availability: {'Yes' if book.availability else 'No'}")

                elif choice == "5":
                    Book.display_all_books()

                elif choice == "6":
                    break
                else:
                    print("Invalid choice, please try again.")

            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            

# User Operations Menu
def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ")

        try:
            if choice == "1":
                name = input("Enter user name: ")
                library_id = input("Enter user library ID: ")

                # Validate library ID (example: alphanumeric check)
                if not re.match(r"^[a-zA-Z0-9]+$", library_id):
                    raise ValueError("Invalid library ID format. It must be alphanumeric.")

                user = User(name, library_id)
                user.save_to_db()
                print(f"User {name} added successfully.") 

            elif choice == "2":
                library_id = input("Enter user library ID: ")
                
                # Validate library ID format
                if not re.match(r"^[a-zA-Z0-9]+$", library_id):
                    raise ValueError("Invalid library ID format.")
                
                user = User.search_by_library_id(library_id)
                if user:
                    print(f"User Found: {user._name}, Library ID: {user._library_id}")
                else:
                    print(f"No user found with Library ID: {library_id}")

            elif choice == "3":
                User.display_all_users()

            elif choice == "4":
                break

            else:
                print("Invalid choice, please try again.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")


            

# Author Operations Menu
def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ")

        try:

            if choice == "1":
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                author = Author(name, biography)
                author.save_to_db()
                print(f"Author {name} added successfully.")
            
            elif choice == "2":
                author_id = input("Enter author ID: ")
                # Validate author ID (example: numeric check)
                if not author_id.isdigit():
                    raise ValueError("Invalid author ID format. It must be numeric.")

                author = Author.search_by_id(author_id)
                if author:
                    print(f"Author Found: {author._name}, Biography: {author._biography}")
                else:
                    print(f"No author found with ID: {author_id}")


            elif choice == "3":
                Author.display_all_authors()

            elif choice == "4":
                break

            else:
                print("Invalid choice, please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")   

# Run the system
if __name__ == "__main__":
    main_menu()

