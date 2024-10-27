import mysql.connector
from db_connection import create_connection

class Book:
    def __init__(self, id, title, author_id, isbn, publication_date, availability=True):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability
    
    def save_to_db(self):
        """Save the book object to the database."""
        connection = create_connection()
        if connection is None:
            print("Connection to database failed.")
            return

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)",
                (self.title, self.author_id, self.isbn, self.publication_date, self.availability)
            )
            connection.commit()
            print("Book added successfully!")

        except mysql.connector.Error as err:
            print(f"Error adding book: {err}")

        finally:
            cursor.close()
            connection.close()
    
   
def add_book(book):
    """Add a new book to the database."""
    connection = create_connection()
    if connection is None:
        print("Connection to database failed.")
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO books (ttitle, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)",
            (book.title, book.author_id, book.isbn, book.publication_date, book.availability)    
        )
        connection.commit()
        print("Book added successfully!")
    
    except mysql.connector.Error as err:
        print(f"Error adding book: {err}")
    
    finally:
        cursor.close()
        connection.close()

def search_by_isbn(isbn):
    """Search for a book by its ISBN."""
    connection = create_connection()
    if connection is None:
        print("Connection to database failed.")
        return None

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
        result = cursor.fetchone()

        if result:
            return Book(id=result[0], title=result[1], author_id=result[2], isbn=result[3], publication_date=result[4], availability=result[5])
        else:
            print("Book not found.")
            return None

    except mysql.connector.Error as err:
        print(f"Error searching for book: {err}")
        return None

    finally:
        cursor.close()
        connection.close()

def display_all_books():
    """Display all books in the library."""
    connection = create_connection()
    if connection is None:
        print("Connection to database failed.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books found in the library.")
            return

        print("\nBooks in the Library:")
        for book in books:
            id, title, author_id, isbn, publication_date, availability = book
            status = "Available" if availability else "Not Available"
            print(f"ID: {id}, Title: {title}, Author ID: {author_id}, ISBN: {isbn}, Date: {publication_date}, Status: {status}")

    except mysql.connector.Error as err:
        print(f"Error retrieving books: {err}")

    finally:
        cursor.close()
        connection.close()



def update_availability(isbn, availability):
    """Update the availability status of a book."""
    connection = create_connection()
    if connection is None:
        print("Connection to database failed.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE books SET availability = %s WHERE isbn = %s",
            (availability, isbn)
        )
        if cursor.rowcount == 0:
            print("No book found with that ISBN.")
        else:
            connection.commit()
            print("Book availability updated successfully!")

    except mysql.connector.Error as err:
        print(f"Error updating availability: {err}")

    finally:
        cursor.close()
        connection.close()   

    