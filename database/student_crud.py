from db_connection import db_connect

conn = db_connect()
cursor = conn.cursor()


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    city = input("Enter student city: ")

    sql = "INSERT INTO students (name, age, city) VALUES (%s, %s, %s)"
    values = (name, age, city)

    cursor.execute(sql, values)
    conn.commit()
    print("Student added successfully!")


def view_students():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("No students found.")


def update_student():
    student_id = int(input("Enter student ID to update: "))
    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    new_city = input("Enter new city: ")

    sql = "UPDATE students SET name = %s, age = %s, city = %s WHERE id = %s"
    values = (new_name, new_age, new_city, student_id)

    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    sql = "DELETE FROM students WHERE id = %s"
    values = (student_id,)

    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def view_student_by_id():
    student_id = int(input("Enter student ID to view: "))

    sql = "SELECT * FROM students WHERE id = %s"
    values = (student_id,)

    cursor.execute(sql, values)
    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Student not found.")


while True:
    print("\n---------- Student CRUD App ----------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View Student by ID")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match choice:
        case 1:
            add_student()
        case 2:
            view_students()
        case 3:
            update_student()
        case 4:
            delete_student()
        case 5:
            view_student_by_id()
        case 6:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")

cursor.close()
conn.close()