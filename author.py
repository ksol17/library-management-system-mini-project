import mysql
from db_connection import create_connection, close_connection

class Author:
    def __init__(self, name, biography, author_id=None):
        self.author_id = author_id
        self.name = name
        self.biography = biography

    def save_to_db(self):
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (self.name, self.biography)

        cursor.execute(query, values)
        connection.commit()

        print(f"Author '{self.name}' added to the database.")
        close_connection(connection)

    def display_all_authors():
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM authors")
        results = cursor.fetchall()

        for row in results:
            print(row)

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
            cursor.execute("SELECT author_id, name, biography FROM authors WHERE author_id = %s", (author_id,))
            result = cursor.fetchone()
            if result:
                author_id, name, biography = result
                return Author(name, biography)
            else:
                print(f"No author found with ID: {author_id}")
                return None
        except mysql.connector.Error as err:
            print(f"Error fetching author by ID: {err}")
            return None
        finally:
            close_connection(connection)
