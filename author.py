import mysql
from db_connection import create_connection, close_connection

class Author:
    def __init__(self, name, biography, id=None):
        self.id = id
        self.name = name
        self.biography = biography

     # Getters

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_biography(self):
        return self.biography

    # String representation
    def __str__(self):
        return f"Name: {self.name}, Biography: {self.biography}"


    def save_to_db(self):
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (self.name, self.biography)

        cursor.execute(query, values)
        connection.commit()

        print(f"Author '{self.name}' added to the database.")
        close_connection(connection)

    @staticmethod
    def display_all_authors():
        connection = create_connection()
        if connection is None:
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM authors")
            results = cursor.fetchall()

            for row in results:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error displaying authors: {err}")
        finally:
            close_connection(connection)

    def view_author_details(author_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM authors WHERE author_id = %s"
        cursor.execute(query, (author_id,))
        author = cursor.fetchone()

        if author:
            print(f"Author Found: {author}")
        else:
            print(f"No author found with ID '{author_id}'.")

        close_connection(connection)

  
    def search_by_id(author_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            # Match the columns with the actual database schema
            cursor.execute("SELECT id, name, biography FROM authors WHERE id = %s", (author_id,))
            result = cursor.fetchone()
            if result:
                id, name, biography = result
                return Author(name=name, biography=biography, id=id)
            else:
                print(f"No author found with ID: {author_id}")
                return None
        except mysql.connector.Error as err:
            print(f"Error fetching author by ID: {err}")
            return None
        finally:
            close_connection(connection)