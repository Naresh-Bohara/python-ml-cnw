from db_connection import connect_db

def add_student(name, age, city):
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            return "Database connection failed."

        cursor = conn.cursor()

        sql = "INSERT INTO students (name, age, city) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, city))
        conn.commit()

        return "Student added successfully."

    except Exception as e:
        return f"Error while adding student: {e}"
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
            return None, "Database connection failed."

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        return records, None

    except Exception as e:
        return None, f"Error while fetching students: {e}"
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def update_student(student_id, new_name, new_age, new_city):
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            return "Database connection failed."

        cursor = conn.cursor()

        sql = "UPDATE students SET name = %s, age = %s, city = %s WHERE id = %s"
        cursor.execute(sql, (new_name, new_age, new_city, student_id))
        conn.commit()

        if cursor.rowcount == 0:
            return "Student not found."

        return "Student updated successfully."

    except Exception as e:
        return f"Error while updating student: {e}"
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def delete_student(student_id):
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            return "Database connection failed."

        cursor = conn.cursor()

        sql = "DELETE FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return "Student not found."

        return "Student deleted successfully."

    except Exception as e:
        return f"Error while deleting student: {e}"
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def view_student_by_id(student_id):
    conn = None
    cursor = None
    try:
        conn = connect_db()
        if conn is None:
            return None, "Database connection failed."

        cursor = conn.cursor()

        sql = "SELECT * FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        record = cursor.fetchone()

        if record is None:
            return None, "Student not found."

        return record, None

    except Exception as e:
        return None, f"Error while searching student: {e}"
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
            try:
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                city = input("Enter student city: ")
                message = add_student(name, age, city)
                print(message)
            except ValueError:
                print("Age must be a number.")

        case 2:
            records, error = view_students()
            if error:
                print(error)
            elif not records:
                print("No students found.")
            else:
                print("\nID\tName\tAge\tCity")
                for row in records:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

        case 3:
            try:
                student_id = int(input("Enter student ID to update: "))
                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))
                new_city = input("Enter new city: ")
                message = update_student(student_id, new_name, new_age, new_city)
                print(message)
            except ValueError:
                print("ID and age must be numbers.")

        case 4:
            try:
                student_id = int(input("Enter student ID to delete: "))
                message = delete_student(student_id)
                print(message)
            except ValueError:
                print("ID must be a number.")

        case 5:
            try:
                student_id = int(input("Enter student ID to view: "))
                record, error = view_student_by_id(student_id)
                if error:
                    print(error)
                else:
                    print("\nID\tName\tAge\tCity")
                    print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")
            except ValueError:
                print("ID must be a number.")

        case 6:
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Please try again.")