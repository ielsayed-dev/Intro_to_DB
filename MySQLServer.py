import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server.
    Handles connection, creation, and proper cleanup.
    """
    connection = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            port=3307
            password='entameen'
        )
        
        if connection.is_connected():
            # Create cursor object
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
            
    except mysql.connector.Error as e:
        # Handle connection and execution errors
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        # Ensure connection is closed properly
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()