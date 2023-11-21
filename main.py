import mysql.connector

from create import create_record
from read import get_all_records
from set_operations import perform_except, perform_intersect, perform_union
from set_comparision import compare_sets_equal_to, compare_sets_greater_than, compare_sets_less_than
from set_membership import check_in_membership, check_exists_membership
from update import update_record
from delete import delete_record
from db_connector import connect_to_database, close_database_connection, get_primary_key

def list_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]
    return tables

def select_table():
    while True:
        print("\n===== Table Selection =====")
        tables = list_tables(db_connection)
        print("Available Tables:")
        for index, table in enumerate(tables):
            print(f"{index + 1}. {table}")

        table_choice = input("Please select the table you wish to work with: ")
        try:
            table_index = int(table_choice) - 1
            if 0 <= table_index < len(tables):
                return tables[table_index]  # Return the selected table name
            else:
                print("Invalid table choice. Please select a valid table.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main_menu():
    while True:
        print("\n===== Road Traffic Management System =====")
        print("1. CRUD Operations")
        print("2. Advanced Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # CRUD Operations Menu
            crud_operations_menu()
        
        elif choice == "2":
            # Advanced Operations Menu
            advanced_operations_menu()
        
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break  # Exit the program
        
        else:
            print("Invalid choice. Please select a valid option.")

def crud_operations_menu():
    table_name = select_table()
    primary_key = get_primary_key(db_connection, table_name)

    if primary_key is None:
        print(f"Table {table_name} does not have a primary key defined.")
        return

    while True:
        print(f"\nTable: {table_name}")
        print("CRUD Operations Menu:")
        print("1. Create (Insert) Record")
        print("2. Read (Retrieve) Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a record
            data = input(f"Enter the values of the record in ({', '.join(get_table_columns(db_connection, table_name))}) format: ")
            values = data.split(',')
            if len(values) != len(get_table_columns(db_connection, table_name)):
                print("Invalid input. Please provide values for all columns.")
            else:
                data_dict = {column: value for column, value in zip(get_table_columns(db_connection, table_name), values)}
                create_record(db_connection, table_name, data_dict)

        elif choice == "2":
            # Read (Retrieve) Records
            records = get_all_records(db_connection, table_name)
            if records:
                print("\nRecords:")
                for index, record in enumerate(records):
                    print(f"Record {index + 1}: {', '.join(f'{key}: {value}' for key, value in record.items())}")
            else:
                print("No records found in the table.")

        elif choice == "3":
            # Update Record
            primary_key_value = input(f"Enter the {primary_key} of the record to update: ")
            data = input(f"Enter the new values of the record in ({', '.join(get_table_columns(db_connection, table_name))}) format: ")
            values = data.split(',')
            if len(values) != len(get_table_columns(db_connection, table_name)):
                print("Invalid input. Please provide values for all columns.")
            else:
                data_dict = {column: value for column, value in zip(get_table_columns(db_connection, table_name), values)}
                update_record(db_connection, table_name, primary_key, primary_key_value, data_dict)

        elif choice == "4":
            # Delete Record
            primary_key_value = input(f"Enter the {primary_key} of the record to delete: ")
            delete_record(db_connection, table_name, primary_key, primary_key_value)

        elif choice == "5":
            # Return to the Main Menu
            break

def advanced_operations_menu():
    while True:
        print("\n===== Advanced Operations Menu =====")
        print("1. Set Operations")
        print("2. Set Membership")
        print("3. Set Comparison")
        print("4. Subqueries with WITH Clause")
        print("5. Advanced Aggregate Functions")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            set_operations_menu()
        
        elif choice == "2":
            set_membership_menu()
        
        elif choice == "3":
            set_comparison_menu()
        
        elif choice == "4":
            subqueries_menu()
        
        elif choice == "5":
            aggregate_functions_menu()
        
        elif choice == "6":
            break  # Return to the Main Menu
        
        else:
            print("Invalid choice. Please select a valid option.")

def set_operations_menu():
    while True:

        print("\n===== Set Operations Menu =====")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference")
        print("4. Back to Advanced Operations Menu")
        choice = input("Enter your choice: ")

        if choice == "4":
            break
        else:
            table_name = select_table()
            print("please select the second table you wish to perform set operations on:")
            second_table = select_table()
            if choice == "1":
                # Perform Union
                print("\nPerforming Union Operation:")
                print(perform_union(db_connection, table_name, second_table))
            
            elif choice == "2":
                # Perform Intersection
                print("\nPerforming Intersection Operation:")
                print(perform_intersect(db_connection, table_name, second_table))
            
            elif choice == "3":
                # Perform Difference
                print("\nPerforming Difference Operation:")
                print(perform_except(db_connection, table_name, second_table))
        
            else:
                print("Invalid choice. Please select a valid option.")

def set_membership_menu():
    while True:
        print("\n===== Set Membership Menu =====")
        print("1. IN Membership Check")
        print("2. EXISTS Membership Check")
        print("3. Back to Advanced Operations Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            # IN Membership Check
            table_name = select_table()
            print("\nPerforming IN Membership Check:")
            column = input("Enter the column to check: ")
            value = input("Enter the value to check: ")
            records = check_in_membership(db_connection, table_name, column, value)
            print_records(records)  # Display or process the membership check results as needed
        
        elif choice == "2":
            table_name = select_table()
            # EXISTS Membership Check
            print("\nPerforming EXISTS Membership Check:")
            condition = input("Enter the condition to check: ")
            records = check_exists_membership(db_connection, table_name, condition)
            print_records(records)  # Display or process the membership check results as needed
        
        elif choice == "3":
            break  # Return to the Advanced Operations Menu
        
        else:
            print("Invalid choice. Please select a valid option.")

def set_comparison_menu():
    while True:
        print("\n===== Set Comparison Menu =====")
        print("1. Less Than Comparison")
        print("2. Greater Than Comparison")
        print("3. Equal To Comparison")
        print("4. Back to Advanced Operations Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Less Than Comparison
            table_name = select_table()
            print("\nPerforming Less Than Comparison:")
            column = input("Enter the column to compare: ")
            threshold = input("Enter the threshold value: ")
            records = compare_sets_less_than(db_connection, table_name, column, threshold)
            print_records(records)  # Display or process the comparison results as needed
        
        elif choice == "2":
            # Greater Than Comparison
            table_name = select_table()
            print("\nPerforming Greater Than Comparison:")
            column = input("Enter the column to compare: ")
            threshold = input("Enter the threshold value: ")
            records = compare_sets_greater_than(db_connection, table_name, column, threshold)
            print_records(records)  # Display or process the comparison results as needed
        
        elif choice == "3":
            # Equal To Comparison
            table_name = select_table()
            print("\nPerforming Equal To Comparison:")
            column = input("Enter the column to compare: ")
            value = input("Enter the value to compare: ")
            records = compare_sets_equal_to(db_connection, table_name, column, value)
            print_records(records)  # Display or process the comparison results as needed
        
        elif choice == "4":
            break  # Return to the Advanced Operations Menu
        
        else:
            print("Invalid choice. Please select a valid option.")

def subqueries_menu():
    while True:
        print("\n===== Subqueries Menu =====")
        print("1.Top 3 Cities with highest population")
        print("2.Top 3 Violation types ")
        print("3.Return to Advance functions menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            query = ("WITH RankedCities AS (SELECT City_name, Population,RANK() OVER (ORDER BY Population DESC) AS "
                   "City_Rank FROM City) SELECT City_name, Population FROM RankedCities WHERE City_Rank <= 3;")
            records = run_custom_query(db_connection, query)
            print_records(records)

        elif choice == "2":
            query = ("WITH RankedType AS ( SELECT distinct Type, dense_rank() OVER (ORDER BY Type DESC) AS Type_Rank "
                   "FROM traffic_violations) SELECT Type FROM RankedType WHERE Type_Rank <= 3;")
            records = run_custom_query(db_connection, query)
            print_records(records)    

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please select a valid option.")

def aggregate_functions_menu():
    while True:
        print("\n===== Aggregate Functions Menu =====")
        print("1. Aggregation: Retrieve the city with the highest population.")
        print("2. Lead/Lag: Show Adjacent Roads")
        print("3. Rollup: No.of incidents across regions ")
        print("4. Rank: Rank roads by their length across all cities in DESC order.")
        print("5. Return to Advance function menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            query = ("SELECT City_name, Population FROM City "
                    " WHERE Population = (SELECT MAX(Population) FROM City);")
            records = run_custom_query(db_connection, query)
            print_records(records)

        elif choice == "2":
            query = ("select Road_name,Previous_Road,Next_Road from ( SELECT Roadid,Road_name, "
                    " LAG(Road_name) OVER (ORDER BY Roadid) AS Previous_Road, LEAD(Road_name) OVER (ORDER BY Roadid) AS Next_Road "
                    " FROM Road) as roadname WHERE Roadid = 4;")
            records = run_custom_query(db_connection, query)
            print_records(records)

        elif choice == "3":
            query = ("SELECT C.city_name,R.RoadType,R.Road_name, sum(TII.incidentid) as Total_incidents from City C "
                    " JOIN Road R on R.cityid=C.cityid  JOIN traffic_incidents TI on R.Roadid=TI.Roadid "
                    " JOIN Traffic_Incidents TII on R.Roadid=TII.Roadid Group by C.City_name,R.RoadType,R.Road_name with rollup;")
            records = run_custom_query(db_connection, query)
            print_records(records)

        elif choice == "4":
            query = ("SELECT C.City_name,Road_name, Length, SUM(Length) OVER (PARTITION BY R.Cityid ORDER BY Roadid) AS "
            " Cumulative_Length FROM Road R JOIN City C ON R.Cityid = C.Cityid;")
            records = run_custom_query(db_connection, query)
            print_records(records)

        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

def get_table_columns(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = [column[0] for column in cursor.fetchall()]
    return columns

def run_custom_query(connection, query):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    except mysql.connector.Error as error:
        print("Error: ", error)

def print_records(records):
    if records:
        print("\nRecords:")
        for index, record in enumerate(records):
            print(f"Record {index + 1}: {', '.join(f'{key}: {value}' for key, value in record.items())}")

if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        main_menu()
        close_database_connection(db_connection)