# Student Management System
# Python + MySQL
import mysql.connector
# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

cursor = db.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks FLOAT
)
""")

# Add Student
def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    sql = "INSERT INTO students VALUES (%s, %s, %s, %s, %s)"
    values = (id, name, age, course, marks)

    cursor.execute(sql, values)
    db.commit()

    print("Student added successfully!\n")

# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n----- Student Records -----")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print(f"Marks: {student[4]}")
        print("--------------------------")

# Search Student
def search_student():
    sid = int(input("Enter Student ID to search: "))

    sql = "SELECT * FROM students WHERE id = %s"
    value = (sid,)

    cursor.execute(sql, value)
    student = cursor.fetchone()

    if student:
        print("\nStudent Found!")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print(f"Marks: {student[4]}")
    else:
        print("Student not found!")

# Update Student
def update_student():
    sid = int(input("Enter Student ID to update: "))

    new_name = input("Enter New Name: ")
    new_age = int(input("Enter New Age: "))
    new_course = input("Enter New Course: ")
    new_marks = float(input("Enter New Marks: "))

    sql = """
    UPDATE students
    SET name=%s, age=%s, course=%s, marks=%s
    WHERE id=%s
    """

    values = (new_name, new_age, new_course, new_marks, sid)

    cursor.execute(sql, values)
    db.commit()

    print("Student updated successfully!")

# Delete Student
def delete_student():
    sid = int(input("Enter Student ID to delete: "))

    sql = "DELETE FROM students WHERE id = %s"
    value = (sid,)

    cursor.execute(sql, value)
    db.commit()

    print("Student deleted successfully!")

# Main Menu
while True:
    print("""
Student Management System:
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")