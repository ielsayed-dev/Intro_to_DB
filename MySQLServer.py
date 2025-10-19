#!/usr/bin/env python3
"""
Python script to connect to a MySQL server and create the 'alx_book_store' database.
It uses 'CREATE DATABASE IF NOT EXISTS' to prevent failure if the database already exists.
"""

import mysql.connector
from mysql.connector import Error

# --- CONFIGURATION ---
# NOTE: Replace 'your_mysql_user' and 'your_mysql_password' with your actual MySQL credentials.
config = {
    'host': 'localhost',
    'user': 'root',
    'port' : 3307,
    'password': 'entameen', 
}

DB_NAME = 'alx_book_store'
connection = None
cursor = None

try:
    # Code to establish a connection to the MySQL server
    print("Attempting to connect to MySQL server...")
    # Establishing connection to the server without specifying a database
    connection = mysql.connector.connect(**config)
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Constructing the required CREATE DATABASE statement
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
        
        # Execute CREATE DATABASE command
        # This explicitly uses the required lowercase database name 'alx_book_store'
        cursor.execute(create_db_query)
        
        # Print success message
        print(f"Database '{DB_NAME}' created successfully!")
        
except Error as e:
    # Code to handle exceptions (connection failure or other MySQL errors)
    print(f"Error: Failed to connect to MySQL server or execute query. Details: {e}")
    
finally:
    # Ensure cursor and connection are closed properly
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()
        # print("MySQL connection closed.")
