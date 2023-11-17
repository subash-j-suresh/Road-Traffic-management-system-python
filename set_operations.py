import mysql.connector

def perform_union(cursor, table_name, table_to_union):
    union_query = f"SELECT * FROM {table_name} UNION SELECT * FROM {table_to_union}"
    try:
        cursor.execute(union_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during UNION operation:", error)
        return []

def perform_intersect(cursor, table_name, table_to_intersect):
    intersect_query = f"SELECT * FROM {table_name} INTERSECT SELECT * FROM {table_to_intersect}"
    try:
        cursor.execute(intersect_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during INTERSECT operation:", error)
        return []

def perform_except(cursor, table_name, table_to_except):
    except_query = f"SELECT * FROM {table_name} EXCEPT SELECT * FROM {table_to_except}"
    try:
        cursor.execute(except_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during EXCEPT operation:", error)
        return []