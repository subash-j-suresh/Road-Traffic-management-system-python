import mysql.connector

def compare_sets_greater_than(connection, table_name, column_name, value_to_compare):
    try:
        cursor = connection.cursor()
        compare_query = f"SELECT * FROM {table_name} WHERE {column_name} > %s"
        cursor.execute(compare_query, (value_to_compare,))
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during set comparison:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def compare_sets_less_than(connection, table_name, column_name, value_to_compare):
    try:
        cursor = connection.cursor()
        compare_query = f"SELECT * FROM {table_name} WHERE {column_name} < %s"
        cursor.execute(compare_query, (value_to_compare,))
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during set comparison:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def compare_sets_equal_to(connection, table_name, column_name, value_to_compare):
    try:
        cursor = connection.cursor()
        compare_query = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
        cursor.execute(compare_query, (value_to_compare,))
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during set comparison:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()