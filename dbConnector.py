from os import environ
import mysql.connector
from mysql.connector import Error

def connectAndExecute(query):
    # Get credentials for our connection
    try:
        credentials_file = open('credentials.txt', 'r')
        host_field = credentials_file.readline().strip()
        database_field = credentials_file.readline().strip()
        user_field = credentials_file.readline().strip()
        password_field = credentials_file.readline().strip()
    except:
    # Or use environment variables on your server
        host_field = environ.get('HOST')
        database_field = environ.get('DB')
        user_field = environ.get('USER')
        password_field = environ.get('PW')

    try:
        connection = mysql.connector.connect(host=host_field,
                                            database=database_field,
                                            user=user_field,
                                            password=password_field)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute(query)
            queryResult = cursor.fetchall()
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return queryResult