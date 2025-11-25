import sqlite3
from faker import Faker

def create_database_connect(db_name="school.db"):
    return sqlite3.connect(db_name)

def create_table(con):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS student(
        name TEXT,
        email TEXT,
        phone INTEGER
    )
    """
    con.execute(create_table_query)
    con.commit()  # Make sure the table creation is saved

def insert_student(con, name, email, phone):
    insert_query = "INSERT INTO student(name, email, phone) VALUES (?, ?, ?)"
    con.execute(insert_query, (name, email, phone))
    con.commit()

def select_students(con):
    select_query = "SELECT * FROM student"
    data = con.execute(select_query)
    return data.fetchall()

# === MAIN SCRIPT ===
connection = create_database_connect()
create_table(connection)  # Ensure table exists

# Insert bulk fake data
fk = Faker()
phone = 35435438989
for _ in range(1, 15):
    username = fk.user_name()
    email = fk.email()
    phone += 1
    insert_student(connection, username, email, phone)

# Select and display data
students = select_students(connection)
for student in students:
    print(student)