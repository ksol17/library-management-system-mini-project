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
