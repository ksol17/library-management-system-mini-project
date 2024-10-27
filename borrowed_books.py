import mysql.connector
from db_connection import create_connection
from datetime import datetime




def borrow_book(user_id, book_id):
    """Borrow a book by creating a record in the borrowed_books table."""
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        borrow_date = datetime.now().date()

        # Insert record into borrowed_books table
        cursor.execute(
            "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)",
            (user_id, book_id, borrow_date)
        )
        connection.commit()
        print("Book borrowed successfully!")

    except mysql.connector.Error as err:
        print(f"Error borrowing book: {err}")

    finally:
        cursor.close()
        connection.close()

def return_book(user_id, book_id):
    """Return a borrowed book by updating the return date in the borrowed_books table."""
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        return_date = datetime.now().date()

        # Update the return date for the borrowed book
        cursor.execute(
            "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date IS NULL",
            (return_date, user_id, book_id)
        )
        if cursor.rowcount == 0:
            print("No borrowed record found for this user and book.")
        else:
            connection.commit()
            print("Book returned successfully!")

    except mysql.connector.Error as err:
        print(f"Error returning book: {err}")

    finally:
        cursor.close()
        connection.close()

def view_borrowed_books(user_id):
    """Display all borrowed books for a specific user."""
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT b.title, bb.borrow_date, bb.return_date "
            "FROM borrowed_books bb JOIN books b ON bb.book_id = b.id "
            "WHERE bb.user_id = %s",
            (user_id,)
        )
        borrowed_books = cursor.fetchall()

        if not borrowed_books:
            print("No borrowed books found for this user.")
        else:
            print("\nBorrowed Books:")
            for title, borrow_date, return_date in borrowed_books:
                status = "Returned" if return_date else "Not Returned"
                print(f"Title: {title}, Borrow Date: {borrow_date}, Return Date: {return_date or 'N/A'}, Status: {status}")

    except mysql.connector.Error as err:
        print(f"Error retrieving borrowed books: {err}")

    finally:
        cursor.close()
        connection.close()
