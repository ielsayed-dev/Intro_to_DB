#!/usr/bin/env python3
"""
Python script to connect to a MySQL server and create the 'alx_book_store' database.
It uses 'CREATE DATABASE IF NOT EXISTS' to prevent failure if the database already exists.
"""

import mysql.connector
from mysql.connector import Error

# --- CONFIGURATION ---
# NOTE: Replace 'your_mysql_user' and 'your_mysql_password' with your actual MySQL credentials.
connection = mysql.connector.connect(
            host='localhost',
            port=3307,  # Docker container port
            user='root',
            password='entameen'  # Change to match your Docker password
        )

DB_NAME = 'alx_book_store'
connection = None
cursor = None

try:
    # 1. Open Connection to MySQL Server
    print("Attempting to connect to MySQL server...")
    connection = mysql.connector.connect(**config)
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # 2. Execute CREATE DATABASE command
        # Using IF NOT EXISTS ensures the script does not fail if the DB already exists.
        create_db_query = "CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME)
        
        # All SQL keywords are capitalized as per previous instructions, though not strictly required by python.
        cursor.execute(create_db_query)
        
        # 3. Print success message
        print(f"Database '{DB_NAME}' created successfully!")
        
except Error as e:
    # 4. Print error message for connection failure
    print(f"Error: Failed to connect to MySQL server. Details: {e}")
    
finally:
    # 5. Handle open and close of the DB connection
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()
        # print("MySQL connection closed.")