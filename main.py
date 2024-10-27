import re
from book import Book, add_book, search_by_isbn, display_all_books, update_availability
from user import User
from author import Author 
from borrowed_books import borrow_book, return_book, view_borrowed_books


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
            print("Exiting Library Management System. Goodbye!")
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
                    title = input("Enter book title: ")
                    author_id = input("Enter author_id: ")
                    isbn = input("Enter ISBN: ")
                    publication_date = input("Enter publication date (YYYY-MM-DD): ")
                        # Validate date format
                    if not re.match(r"\d{4}-\d{2}-\d{2}", publication_date):
                        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

                    # Create and save the book
                    new_book = Book(None, title, author_id, isbn, publication_date)
                    new_book.save_to_db()
                    print("Book added successfully.")

                elif choice == "2":
                    isbn = input("Enter ISBN of the book to borrow: ")
                    book = search_by_isbn(isbn)
                    if book:
                        update_availability(isbn, False)
                        print(f"Book '{book.title}' marked as borrowed.")
                    else:
                        print("Book not found.")


                elif choice == "3":
                    isbn = input("Enter ISBN of the book to return: ")
                    book = search_by_isbn(isbn)
                    if book:
                        update_availability(isbn, True)
                        print(f"Book '{book.title}' marked as available.")
                    else:
                        print("Book not found.")

                elif choice == "4":
                    isbn = input("Enter ISBN to search: ")
                    book = search_by_isbn(isbn)
                    if book:
                        print(f"Book Found: {book.title}, Author ID: {book.author_id}, Availability: {'Yes' if book.availability else 'No'}")
                    else:
                        print("Book not found")

                elif choice == "5":
                    display_all_books()

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
                user = User(name, library_id)
                user.save_to_db()
                print(f"User {name} added successfully.")

            elif choice == "2":
                library_id = input("Enter user library ID: ")
                if not re.match(r"^[a-zA-Z0-9]+$", library_id):
                    print("Invalid library ID format.")
                    continue  # Go back to the menu or loop

                user = User.search_by_library_id(library_id)  # This correctly provides the argument
                if user:
                    print(f"User Found: {user.name}, Library ID: {user.library_id}")
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
                # Validate inputs
                if not name.strip():
                    print("Author name cannot be empty.")
                    continue
                
                if not biography.strip():
                    print("Author biography cannot be empty.")
                    continue

                # Create the author object without an ID, assuming it’s auto-generated
                author = Author(name=name, biography=biography)

                # Save to the database
                author.save_to_db()
                print(f"Author {name} added successfully.")
            
            elif choice == "2":
                id_input = input("Enter ID: ")
                # Validate author ID (example: numeric check)
                if not id_input.isdigit():
                    raise ValueError("Invalid author ID format. It must be numeric.")
                    continue
                
                # Convert the ID to an integer
                author_id = int(id_input)

                author = Author.search_by_id(author_id)
                if author:
                    print(f"Author Found: {author.get_name()}, Biography: {author.get_biography()}")
                else:
                    print(f"No author found with ID: {id}")


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

