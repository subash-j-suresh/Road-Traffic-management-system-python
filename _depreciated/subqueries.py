import mysql.connector

def execute_query_with_cte(connection, main_query):
    """
    Executes a SQL query containing a Common Table Expression (CTE) with the WITH clause.

    Args:
    - connection: MySQL database connection object.
    - main_query (str): SQL query string with the WITH clause.

    Returns:
    - list: List of records retrieved from the executed query.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(main_query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print("Error during query execution:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()