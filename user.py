import mysql.connector
from db_connection import create_connection, close_connection

class User:
    def __init__(self, name, library_id, id=None):
        self.name = name
        self.library_id = library_id
        self.id = id

    # Getters
    def get_name(self):
        return self.name
    
    def get_library_id(self):
        return self.library_id
    
    
    # Methods
    def borrow_book(self, book):
        if book.is_available():
            self._borrowed_books.append(book.get_title())
            book.set_availability(False)
            print(f"{book.get_title()} has been borrowed by {self.name}.")
        else:
            print("The book is not available.")
    
    def return_book(self, book):
        if book.get_title() in self._borrowed_books:
            self._borrowed_books.remove(book.get_title())
            book.set_availability(True)
            print(f"{book.get_title()} has been returned by {self.name}.")
        else:
            print("This user did not borrow this book.")

    @classmethod
    def search_by_library_id(cls, library_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id, name, library_id FROM users WHERE library_id = %s", (library_id,))
            result = cursor.fetchone()
            if result:
               # Unpack and create an instance only if result is not None
               user_id, name, library_id = result
               return cls(name, library_id, user_id)
            else:
                print(f"No user found with Library ID: {library_id}")
                return None
        except mysql.connector.Error as err:
            print(f"Error fetching user by Library ID: {err}")
            return None
        finally:
            close_connection(connection)


    # String representation
    def __str__(self):
        return f"Name: {self.name}, Library ID: {self.library_id}"


    def save_to_db(self):
        connection = create_connection()
        if connection is None:
            return
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            values = (self.name, self.library_id)
            cursor.execute(query, values)
            connection.commit()
            print(f"User '{self.name}' added to the database.")
        except mysql.connector.Error as err:
            print(f"Error adding user to database: {err}")
        finally:
            close_connection(connection)

    @staticmethod
    def display_all_users():
        connection = create_connection()
        if connection is None:
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()

            for row in results:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error displaying users: {err}")
        finally:
            close_connection(connection)


    def view_user_details(self, library_id):
        connection = create_connection()
        if connection is None:
            return

        try:
            cursor = connection.cursor()
            query = "SELECT id, name, library_id FROM users WHERE library_id = %s"
            cursor.execute(query, (library_id,))
            user = cursor.fetchone()

            if user:
                # Access user details by index
                user_id, name, lib_id = user
                print(f"User Found: Name: {name}, Library ID: {lib_id}")
            else:
                print(f"No user found with library ID '{library_id}'.")
        except mysql.connector.Error as err:
            print(f"Error viewing user details: {err}")
        finally:
            close_connection(connection)
 
