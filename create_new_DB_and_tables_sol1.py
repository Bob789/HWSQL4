# Solution 1
import sqlite3

try:
    # Variable for checking if there is no problem with SQL
    success = False

    # Create a new database
    db_name = "HWSQL4.08.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Create a 'students' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')

    # Create a 'courses' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            hours INTEGER NOT NULL
        );
    ''')

    # Create a 'grades' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            course_id INTEGER,
            student_id INTEGER,
            grade INTEGER,
            PRIMARY KEY(course_id, student_id),
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id)
        );
    ''')

    # If everything runs successfully, set success to True
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
        print(f"Database '{db_name}' created successfully!")
        print("Table 'students' created successfully!")
        print("Table 'courses' created successfully!")
        print("Table 'grades' created successfully!")
    else:
        print("Failed to create the database or tables.")
