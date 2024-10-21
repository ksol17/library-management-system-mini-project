from db_connection import create_connection, close_connection

class Book:
    def __init__(self, title, author_id, isbn, pub_date, book_id=None, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.pub_date = pub_date
        self.is_available = is_available

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
        connection = create_connection()
        cursor = connection.cursor()

        query = "UPDATE Books SET is_availabe = %s WHERE isbn = %s"
        cursor.execute(query, (False, self.isbn))
        connection.commit()
        
        print(f"Book '{self.title}' marked as borrowed.")
        close_connection(connection)
    
    def mark_returned(self):
        connection = create_connection()
        cursor = connection.cursor()

        query = "UPDATE Books SET is_available = %s WHERE isbn = %s"
        cursor.execute(query, (True, self.isbn))
        connection.commit()

        print(f"Book '{self.title}' marked as returned.")
        close_connection(connection)

    
    def search_by_isbn(isbn):
        connection = create_connection()
        cursor = connection.cursor()
        
        query = "SELECT * FROM Books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        book = cursor.fetchone()

        if book:
            print(f"Book found: {book}")
        else:
            print(f"No book found with ISBN '{isbn}'.")   
        close_connection(connection)


    def display_all_books():
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Books")
        results = cursor.fetchall

        close_connection(connection)