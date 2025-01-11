# 2 Solution
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

    # Insert multiple rows using a list of tuples
    data_to_insert = [
        ('Avi', 'aa1@bbb.com'),
        ('Miki', 'aa2@bbb.com'),
        ('Riki', 'aa3@bbb.com'),
        ('Lee', 'aa4@bbb.com'),
        ('Shay', 'aa5@bbb.com'),
        ('Rotem', 'aa6@bbb.com')
    ]

    # Insert Rows to students table
    cursor.executemany('''
        INSERT INTO students (name, email)
        VALUES (?, ?)
    ''', data_to_insert)

    # Insert multiple rows using a list of tuples
    data_to_insert = [
        ('Math', 181),
        ('Sociology', 182),
        ('English', 183),
        ('AI', 184),
        ('Business', 185),
        ('Geographic', 186)
    ]

    # Insert Rows to courses table
    cursor.executemany('''
        INSERT INTO courses (topic, hours)
        VALUES (?, ?)
    ''', data_to_insert)

    # Insert multiple rows using a list of tuples
    data_to_insert = [
        (2, 5, 81),
        (1, 4, 82),
        (3, 1, 83),
        (4, 2, 84),
        (6, 3, 85),
        (5, 6, 86),
        (5, 4, 97),
        (6, 2, 98),
        (1, 1, 99),
        (1, 2, 100),
    ]

    # Insert Rows to grades table
    cursor.executemany('''
        INSERT INTO grades (course_id, student_id, grade)
        VALUES (?, ?, ?)
    ''', data_to_insert)

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
        print("Data insert to table students successfully!")
        print("Data insert to table courses successfully!")
        print("Data insert to table grades successfully!")
    else:
        print("Failed to enter data to tables.")
