import mysql.connector
from db_connector import connect_to_database, close_database_connection

def update_record(connection, table_name, primary_key_name, primary_key_value, data):
    try:
        cursor = connection.cursor()

        # SQL update statement
        columns = ', '.join(data.keys())
        placeholders = ', '.join([f"{col} = %s" for col in data])
        update_query = f"UPDATE {table_name} SET {placeholders} WHERE {primary_key_name} = %s"

        # Data to be updated
        record_data = tuple(data.values()) + (primary_key_value,)

        cursor.execute(update_query, record_data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Record with {primary_key_name} {primary_key_value} updated successfully")
        else:
            print(f"No record with {primary_key_name} {primary_key_value} found for update")

    except mysql.connector.Error as error:
        print("Error:", error)
        connection.rollback()
