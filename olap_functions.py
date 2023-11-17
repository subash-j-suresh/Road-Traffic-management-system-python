import mysql.connector

def calculate_rollup(connection, table_name, columns):
    """
    Performs the ROLLUP operation on specified columns.

    Args:
    - connection: MySQL database connection object.
    - table_name (str): Name of the table.
    - columns (str): Columns to perform ROLLUP on.

    Returns:
    - list: List of tuples containing aggregated values for each rollup.
    """
    try:
        cursor = connection.cursor()
        rollup_query = f"SELECT {columns}, SUM(column_name) FROM {table_name} GROUP BY ROLLUP({columns})"
        cursor.execute(rollup_query)
        rollup_values = cursor.fetchall()
        return rollup_values
    except mysql.connector.Error as error:
        print("Error during ROLLUP calculation:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def calculate_cube(connection, table_name, columns):
    """
    Performs the CUBE operation on specified columns.

    Args:
    - connection: MySQL database connection object.
    - table_name (str): Name of the table.
    - columns (str): Columns to perform CUBE on.

    Returns:
    - list: List of tuples containing aggregated values for each cube.
    """
    try:
        cursor = connection.cursor()
        cube_query = f"SELECT {columns}, SUM(column_name) FROM {table_name} GROUP BY CUBE({columns})"
        cursor.execute(cube_query)
        cube_values = cursor.fetchall()
        return cube_values
    except mysql.connector.Error as error:
        print("Error during CUBE calculation:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def calculate_grouping_sets(connection, table_name, columns):
    """
    Performs the GROUPING SETS operation on specified columns.

    Args:
    - connection: MySQL database connection object.
    - table_name (str): Name of the table.
    - columns (str): Columns to perform GROUPING SETS on.

    Returns:
    - list: List of tuples containing aggregated values for each grouping set.
    """
    try:
        cursor = connection.cursor()
        grouping_sets_query = f"SELECT {columns}, SUM(column_name) FROM {table_name} GROUP BY GROUPING SETS({columns})"
        cursor.execute(grouping_sets_query)
        grouping_sets_values = cursor.fetchall()
        return grouping_sets_values
    except mysql.connector.Error as error:
        print("Error during GROUPING SETS calculation:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()