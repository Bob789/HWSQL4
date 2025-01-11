# 5 Solution
import sqlite3
try:
    # variable for checking if there is no problem SQL
    success = False

    # Data to display
    row_title = ['Course Topic', 'Hours']

    # Insert row
    row_data = []

    # Ask the user for data to insert into the courses table
    row_data.append(str(input("Enter the course topic to update the table: ")) )
    row_data.append(int(input("Enter the number of hours for the course to update the table: ")))

    # Define database which have 3 table (students, courses, grades)
    db_name = "HWSQL4.08.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # # Select rows to UPDATE base on topic
    cursor.execute('''
        SELECT * FROM courses 
        WHERE topic = ?
    ''',(row_data[0],))

    # Print rows selected
    row_to_update = cursor.fetchone()

    # Display the row that will be update
    if not row_to_update:

        # Insert Rows to courses table
        cursor.execute('''
                INSERT INTO courses (topic, hours)
                VALUES (?, ?)
            ''', row_data)

        print("The following row has been inserted:")
        # Print title row
        print(f"{row_title[0]:<20} {row_title[1]:<10}")
        # Print data row
        print(f"{row_data[0]:<20} {row_data[1]:<10}")
        print("Row update successfully!")
        success = True
    else:
        print(f"It is already exists: {row_data[0]} NO UPDATE EXECUTE!!! ")

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection properly
    if conn:
        if success:
            # Commit only if a new row was inserted
            conn.commit()
        conn.close()
        print("Database connection closed.")