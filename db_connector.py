import mysql.connector
from db_config import DB_CONFIG

def connect_to_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Failed to connect to the database")

    except mysql.connector.Error as error:
        print("Error: ", error)

    return None


def close_database_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

def get_primary_key(connection, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'")
        primary_key = cursor.fetchone()
        if primary_key:
            return primary_key[4]
        return None
    except mysql.connector.Error as error:
        print("Error:", error)
        return None


