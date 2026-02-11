import os

FILE_PATH = "students-info.txt"

# ---------------- Validation ---------------- #

def validate_text(value, field, min_chars=1):
    value = value.strip()
    if not value:
        raise ValueError(f"{field} cannot be empty.")
    if len(value) < min_chars:
        raise ValueError(f"{field} must be at least {min_chars} characters.")
    return value


def validate_email(email):
    email = email.strip().lower()
    if not email.endswith("@gmail.com"):
        raise ValueError("Email must end with @gmail.com")
    return email


def validate_age(age):
    age = int(age)
    if not (5 <= age <= 105):
        raise ValueError("Age must be between 5 and 105.")
    return str(age)


# ---------------- File Helpers ---------------- #

def read_students():
    students = []
    try:
        with open(FILE_PATH, "r") as file:
            for line in file:
                students.append(line.strip().split(","))
    except FileNotFoundError:
        open(FILE_PATH, "a").close()
    return students


def write_students(students):
    with open(FILE_PATH, "w") as file:
        for s in students:
            file.write(",".join(s) + "\n")


# ---------------- CRUD ---------------- #

def add_student():
    try:
        sid = validate_text(input("ID: "), "ID")
        name = validate_text(input("Name: "), "Name", 3)
        age = validate_age(input("Age: "))
        email = validate_email(input("Email: "))
        address = validate_text(input("Address: "), "Address", 3)

        students = read_students()
        for s in students:
            if s[0] == sid:
                raise ValueError("Student ID already exists.")

        with open(FILE_PATH, "a") as file:
            file.write(f"{sid},{name},{age},{email},{address}\n")

        print("Student added successfully.")

    except Exception as e:
        print("Error:", e)


def view_all():
    try:
        students = read_students()
        if not students:
            print("No students found.")
            return

        for s in students:
            print(f"ID:{s[0]} | Name:{s[1]} | Age:{s[2]} | Email:{s[3]} | Address:{s[4]}")

    except Exception as e:
        print("Error:", e)


def view_by_id():
    try:
        sid = input("Enter ID: ").strip()
        students = read_students()

        for s in students:
            if s[0] == sid:
                print(f"ID:{s[0]} | Name:{s[1]} | Age:{s[2]} | Email:{s[3]} | Address:{s[4]}")
                return

        print("Student not found.")

    except Exception as e:
        print("Error:", e)


def update_student():
    try:
        sid = input("Enter ID to update: ").strip()
        students = read_students()
        found = False

        for s in students:
            if s[0] == sid:
                found = True
                print("Press Enter to keep old value.")

                name = input(f"New Name ({s[1]}): ").strip()
                if name:
                    s[1] = validate_text(name, "Name", 3)

                age = input(f"New Age ({s[2]}): ").strip()
                if age:
                    s[2] = validate_age(age)

                email = input(f"New Email ({s[3]}): ").strip()
                if email:
                    s[3] = validate_email(email)

                address = input(f"New Address ({s[4]}): ").strip()
                if address:
                    s[4] = validate_text(address, "Address", 3)

        if not found:
            print("Student not found.")
            return

        write_students(students)
        print("Student updated successfully.")

    except Exception as e:
        print("Error:", e)


def delete_student():
    try:
        sid = input("Enter ID to delete: ").strip()
        students = read_students()
        new_students = [s for s in students if s[0] != sid]

        if len(students) == len(new_students):
            print("Student not found.")
            return

        write_students(new_students)
        print("Student deleted successfully.")

    except Exception as e:
        print("Error:", e)


def search_student():
    try:
        term = input("Search: ").lower()
        students = read_students()
        found = False

        for s in students:
            if any(term in field.lower() for field in s):
                print(f"ID:{s[0]} | Name:{s[1]} | Age:{s[2]} | Email:{s[3]} | Address:{s[4]}")
                found = True

        if not found:
            print("No matching student found.")

    except Exception as e:
        print("Error:", e)


# ---------------- MAIN ---------------- #

def main():
    while True:
        print("""
1. Add Student
2. View All Students
3. View Student by ID
4. Update Student
5. Delete Student
6. Search Student
7. Exit
""")

        try:
            choice = int(input("Enter choice (1-7): "))
        except ValueError:
            print("Enter valid number.")
            continue

        match choice:
            case 1:
                add_student()
            case 2:
                view_all()
            case 3:
                view_by_id()
            case 4:
                update_student()
            case 5:
                delete_student()
            case 6:
                search_student()
            case 7:
                print("Exiting...")
                break
            case _:
                print("Invalid choice.")

main()
