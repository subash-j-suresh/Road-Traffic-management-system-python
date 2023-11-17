import mysql.connector

def delete_record(connection, table_name, primary_key, record_id):
    try:
        cursor = connection.cursor()

        # SQL delete statement
        delete_query = f"DELETE FROM {table_name} WHERE {primary_key} = %s"
        
        # Data to specify the record to delete
        record_data = (record_id,)

        cursor.execute(delete_query, record_data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Record with {primary_key} {record_id} deleted successfully from {table_name}")
        else:
            print(f"No record with {primary_key} {record_id} found for deletion in {table_name}")

    except mysql.connector.Error as error:
        print("Error: ", error)
        connection.rollback()
