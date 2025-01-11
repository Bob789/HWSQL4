# 4 Solution
import sqlite3
try:
    # variable for checking if there is no problem SQL
    success = False

    # Define database which have 3 table (students, courses, grades)
    db_name = "HWSQL4.08.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Calculate AVERAGE for each COURSES
    cursor.execute('''
        SELECT course_id AS Line,
        topic AS Course_Name
        FROM courses;
    ''')

    # Fetch the column names from the cursor
    column_titles = [description[0] for description in cursor.description]
    print(column_titles)

    # Print rows selected
    rows = cursor.fetchall()
    result_list = [list(row) for row in rows]

    for result in result_list:
        print(result)

    print("Data Rows are fetchall successfully!")

    success = True

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    if success:
        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # Print success messages
        print("successfully!")
    else:
        print("Failed")
