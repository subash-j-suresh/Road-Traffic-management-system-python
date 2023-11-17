import mysql.connector

def perform_union(connection, table_name, table_to_union):
    union_query = f"SELECT * FROM {table_name} UNION SELECT * FROM {table_to_union}"
    try:
        cursor = connection.cursor()
        cursor.execute(union_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during UNION operation:", error)
        return []

def perform_intersect(connection, table_name, table_to_intersect):
    intersect_query = f"SELECT * FROM {table_name} INTERSECT SELECT * FROM {table_to_intersect}"
    try:
        cursor = connection.cursor()
        cursor.execute(intersect_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during INTERSECT operation:", error)
        return []

def perform_except(connection, table_name, table_to_except):
    except_query = f"SELECT * FROM {table_name} EXCEPT SELECT * FROM {table_to_except}"
    try:
        cursor = connection.cursor()
        cursor.execute(except_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during EXCEPT operation:", error)
        return []