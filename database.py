
import sqlite3

def connect_db():
    return sqlite3.connect("student.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            marks REAL
        )
    """)

    conn.commit()
    conn.close()

create_table()

print("Database and Table Created Successfully!")
