import mysql.connector
from db_connection import create_connection, close_connection

class Book:
    def __init__(self, isbn, title, author, genre, pub_date, availability=True):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._genre = genre
        self._pub_date = pub_date
        self._availability = availability



    def isbn(self):
        return self._isbn
    
    def availability(self):
        return self._availability
    
    def mark_borrowed(self):
        if self._availability:
            self._availability = False
            connection = create_connection()
            cursor = connection.cursor()
            try:
                cursor.execute("UPDATE Books SET availability = %s WHERE isbn = %s", (True, self._isbn))
                connection.commit()
                print(f"Book {self._title} has been borrowed.")
            except mysql.connector.Error as err:
                print(f"Error borrowing the book: {err}")
            finally:
                close_connection(connection)
        else:
            print(f"The book {self._title} is currently unavailable.")

    def save_to_db(self):
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO Books (title, author_id, isbn, pub_date, is_available) VALUES (%s, %s, %s, %s, %s)"
        values = (self.title, self. author_id, self.isbn, self.pub_date, self.is_available)
    
        cursor.execute(query, values)
        connection.commit()

        print(f"Book '{self.title}' with ISBN '{self.isbn}' added to the database.")
        close_connection(connection)

    def mark_borrowed(self):
        if self._availability:
            self._availability = False
            connection = create_connection()
            cursor = connection.cursor()
            try:
                cursor.execute("UPDATE Books SET availability = %s WHERE isbn = %s")
                connection.commit()
                print(f"Book {self._title} has been borrowed.")
            except mysql.connector.Error as err:
                print(f"Error borrowing the book: {err}")
            finally:
                close_connection(connection)
        else:
            print(f"The book {self._title} is currently unavailable.")
        
       
    
    def mark_returned(self):
        if not self._availability:
            self._availability = True
            connection = create_connection()
            cursor = connection.cursor()
            try:
                cursor.execute("UPDATE books SET availability = %s WHERE isbn = %s", (True, self._isbn))
                connection.commit()
                print(f"Book {self._title} has been returned.")
            except mysql.connector.Error as err:
                print(f"Error returning the book: {err}")
            finally:
                close_connection(connection)
        else:
            print(f"The book {self._title} was not borrowed.")

    
    def search_by_isbn(isbn):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT isbn, title, author, genre, pub_date, availability FROM books WHERE isbn = %s", (isbn,))
            result = cursor.fetchone()
            if result:
                isbn, title, author, genre, pub_date, availability = result
                return Book(isbn, title, author, genre, pub_date, availability)
            else:
                print(f"No book found with ISBN: {isbn}")
                return None
        except mysql.connector.Error as err:
            print(f"Error fetching book by ISBN: {err}")
            return None
        finally:
            close_connection(connection)



    def display_all_books():
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            if books:
                print("All Books in the Library:")
                for book in books:
                    print(book)
            else:
                print("No books available in the library.")
        except mysql.connector.Error as err:
            print(f"Error displaying books: {err}")
        finally:
            close_connection(connection)