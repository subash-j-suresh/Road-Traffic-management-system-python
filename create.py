from db_connector import connect_to_database, close_database_connection
import mysql.connector

def create_record(connection, table_name, data):
    try:
        cursor = connection.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s' for _ in data])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        record_data = tuple(data.values())
        cursor.execute(insert_query, record_data)
        connection.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as error:
        print("Error:", error)
        connection.rollback()