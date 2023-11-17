import mysql.connector

def check_in_membership(connection, table_name, column_name, value_to_check):
    try:
        cursor = connection.cursor()
        check_in_query = f"SELECT * FROM {table_name} WHERE {column_name} IN (%s)"
        cursor.execute(check_in_query, (value_to_check,))
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during IN membership check:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def check_exists_membership(connection, table_name, condition):
    try:
        cursor = connection.cursor()
        exists_query = f"SELECT * FROM {table_name} WHERE EXISTS ({condition})"
        cursor.execute(exists_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during EXISTS membership check:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()