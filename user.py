import mysql
from db_connection import create_connection, close_connection

class User:
    def __init__(self, name, library_id, user_id=None):
        self.user_id = user_id
        self.name = name
        self.library_id = library_id

    def save_to_db(self):
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        values = (self.name, self.library_id)

        cursor.execute(query, values)
        connection.commit()

        print(f"User '{self.name}' added to the database.")
        close_connection(connection)


    def display_all_users():
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        for row in results:
            print(row)
        
        close_connection(connection)


    def view_user_details(library_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE library_id = %s"
        cursor.execute(query, (library_id,))
        user = cursor.fetchone()

        if user:
            print(f"User Found: {user}")
        else:
            print(f"No user found with library ID '{library_id}'.")

        close_connection(connection)

    
    def search_by_library_id(library_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT library_id, name FROM users WHERE library_id = %s", (library_id,))
            result = cursor.fetchone()
            if result:
                library_id, name = result
                return User(name, library_id)
            else:
                print(f"No user found with Library ID: {library_id}")
                return None
        except mysql.connector.Error as err:
            print(f"Error fetching user by Library ID: {err}")
            return None
        finally:
            close_connection(connection)

