import mysql.connector
from mysql.connector import Error

def create_connection():
    """Connect to the MySQL database and return the connection object """
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            database = "bookstore_db",
            user = "root",
            password = "Preciosa2016!"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None
    

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")