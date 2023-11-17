import mysql.connector
from db_connector import connect_to_database, close_database_connection

def get_all_records(connection, table_name):
    try:
        cursor = connection.cursor(dictionary=True)
        select_query = f"SELECT * FROM {table_name}"
        cursor.execute(select_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error:", error)
