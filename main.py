
import sqlite3

def connect_db():
    return sqlite3.connect("student.db")


# 1. Add Student
def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO students
        (name, age, department, marks)
        VALUES (?, ?, ?, ?)""",
        (name, age, department, marks)
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully!")


# 2. View Students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- Student Records ---")

    for student in records:
        print(student)

    if not records:
        print("No Student Records Found.")

    conn.close()


# 3. Search Student
def search_student():
    student_id = int(input("Enter Student ID: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    record = cursor.fetchone()

    if record:
        print("Student Found:", record)
    else:
        print("Student Not Found!")

    conn.close()


# 4. Update Student
def update_student():
    student_id = int(input("Enter Student ID: "))
    marks = float(input("Enter New Marks: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks = ? WHERE student_id = ?",
        (marks, student_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")

    conn.close()


# 5. Delete Student
def delete_student():
    student_id = int(input("Enter Student ID: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

    conn.close()


# 6. Calculate Average Marks
def average_marks():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(marks) FROM students")
    result = cursor.fetchone()[0]

    if result is not None:
        print("Average Marks:", round(result, 2))
    else:
        print("No Marks Available.")

    conn.close()


# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

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
        average_marks()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")
