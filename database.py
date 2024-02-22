import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursordb = mydb.cursor()

try:
    # Create the 'school' database if it doesn't exist
    db_creation_query = "CREATE DATABASE IF NOT EXISTS school"
    cursordb.execute(db_creation_query)
    print("Database created")

except mysql.connector.Error as err:
    print("Database creation error:", err)

cursordb.execute("USE school")

# Create a table if it not exist
try:
    cursordb.execute("CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), age INT, grade FLOAT)")
    print("Table created")
except mysql.connector.Error as err:
    print("Table creation error:", err)

# Insert a new student record for Alice Smith
try:
    insert_query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    student_data = ("Alice", "Smith", 18, 95.5)
    cursordb.execute(insert_query, student_data)
    mydb.commit()
    print("Student record for Alice Smith inserted.")
except mysql.connector.Error as err:
    print("Insertion error:", err)

# Insert a new student record for Sonu Kumar
try:
    insert_query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    student_data = ("Sonu", "Kumar", 18, 85)
    cursordb.execute(insert_query, student_data)
    mydb.commit()
    print("Student record for Sonu Kumar inserted.")
except mysql.connector.Error as err:
    print("Insertion error:", err)

# Update the grade of the student with first name "Alice"
try:
    update_query = "UPDATE students SET grade = %s WHERE first_name = %s"
    update_data = (97.0, "Alice")
    cursordb.execute(update_query, update_data)
    mydb.commit()
    print("Grade updated for Alice.")
except mysql.connector.Error as err:
    print("Update error:", err)

# for Delete the student with last name "Smith"
try:
    delete_query = "DELETE FROM students WHERE last_name = %s"
    delete_data = ("Smith",)
    cursordb.execute(delete_query, delete_data)
    mydb.commit()
    print("Student with last name Smith deleted.")
except mysql.connector.Error as err:
    print("Deletion error:", err)

# Fetch and display all student records
try:
    cursordb.execute("SELECT * FROM students")
    records = cursordb.fetchall()

    print("\nAll student records:")
    for record in records:
        print(record)
except mysql.connector.Error as err:
    print("Fetch error:", err)

# Close the connection
mydb.close()