import mysql.connector

def calculate_row_number(connection, table_name, order_by_column):
    """
    Calculates the row number based on the order specified by a column.

    Args:
    - connection: MySQL database connection object.
    - table_name (str): Name of the table.
    - order_by_column (str): Column to use for ordering.

    Returns:
    - list: List of tuples containing (row_number, column_values) for each row.
    """
    try:
        cursor = connection.cursor()
        row_number_query = f"SELECT ROW_NUMBER() OVER (ORDER BY {order_by_column}), * FROM {table_name}"
        cursor.execute(row_number_query)
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as error:
        print("Error during ROW_NUMBER calculation:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def calculate_rank(connection, table_name, partition_column, order_by_column):
    """
    Calculates the rank within each partition based on specified columns.

    Args:
    - connection: MySQL database connection object.
    - table_name (str): Name of the table.
    - partition_column (str): Column used for partitioning.
    - order_by_column (str): Column to use for ordering.

    Returns:
    - list: List of tuples containing (rank, partition_values, ordered_column_values) for each row.
    """
    try:
        cursor = connection.cursor()
        rank_query = f"SELECT RANK() OVER (PARTITION BY {partition_column} ORDER BY {order_by_column}), " \
                     f"{partition_column}, {order_by_column} FROM {table_name}"
        cursor.execute(rank_query)
        ranks = cursor.fetchall()
        return ranks
    except mysql.connector.Error as error:
        print("Error during RANK calculation:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

def calculate_lead_lag(connection, table_name, column_name, offset, default_value=None):
    """
    Calculates the value of a column at a specified offset ahead or behind.

    Args:
    - connection: MySQL database connection object.
    - table_name (str): Name of the table.
    - column_name (str): Column for which LEAD or LAG is calculated.
    - offset (int): Number of rows ahead (positive) or behind (negative) to look for the value.
    - default_value (any): Default value if the offset goes beyond the data.

    Returns:
    - list: List of tuples containing (column_value, lead_or_lag_value) for each row.
    """
    try:
        cursor = connection.cursor()
        default_part = f"DEFAULT '{default_value}'" if default_value is not None else ""
        lead_lag_query = f"SELECT {column_name}, " \
                         f"LEAD({column_name}, {offset}, {default_part}) OVER (ORDER BY {column_name}), " \
                         f"LAG({column_name}, {offset}, {default_part}) OVER (ORDER BY {column_name}) " \
                         f"FROM {table_name}"
        cursor.execute(lead_lag_query)
        lead_lag_values = cursor.fetchall()
        return lead_lag_values
    except mysql.connector.Error as error:
        print("Error during LEAD/LAG calculation:", error)
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()

