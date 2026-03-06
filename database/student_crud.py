from db_connection import connect_db


def add_student():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            print("Database connection failed.")
            return

        cursor = conn.cursor()

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        city = input("Enter student city: ")

        sql = "INSERT INTO students (name, age, city) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, city))
        conn.commit()

        print("Student added successfully.")

    except ValueError:
        print("Age must be a number.")
    except Exception as e:
        print("Error while adding student:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def view_students():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            print("Database connection failed.")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        if not records:
            print("No students found.")
            return

        print("\nID\tName\tAge\tCity")
        for row in records:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

    except Exception as e:
        print("Error while fetching students:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def update_student():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            print("Database connection failed.")
            return

        cursor = conn.cursor()

        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_city = input("Enter new city: ")

        sql = "UPDATE students SET name = %s, age = %s, city = %s WHERE id = %s"
        cursor.execute(sql, (new_name, new_age, new_city, student_id))
        conn.commit()

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student updated successfully.")

    except ValueError:
        print("ID and age must be numbers.")
    except Exception as e:
        print("Error while updating student:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def delete_student():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            print("Database connection failed.")
            return

        cursor = conn.cursor()

        student_id = int(input("Enter student ID to delete: "))

        sql = "DELETE FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student deleted successfully.")

    except ValueError:
        print("ID must be a number.")
    except Exception as e:
        print("Error while deleting student:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def view_student_by_id():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            print("Database connection failed.")
            return

        cursor = conn.cursor()

        student_id = int(input("Enter student ID to view: "))

        sql = "SELECT * FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        record = cursor.fetchone()

        if record is None:
            print("Student not found.")
        else:
            print("\nID\tName\tAge\tCity")
            print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")

    except ValueError:
        print("ID must be a number.")
    except Exception as e:
        print("Error while searching student:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


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