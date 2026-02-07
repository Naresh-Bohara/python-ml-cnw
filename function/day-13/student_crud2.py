students = {}

def add_student():
    sid = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip().title()
    age = int(input("Enter Student Age: ").strip())
    address = input("Enter Student Address: ").strip().title()

    students[sid] = {
        "name": name,
        "age": age,
        "address": address
    }
    print(f"Student {name} added successfully.")

def view_students():
    if not students:
        print("No students found.")
        return

    print("Student List:")
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Address: {info['address']}")

def update_student():
    sid = input("Enter Student ID to update: ").strip()
    if sid not in students:
        print("No student found.")
        return

    name = input("Enter new Student Name: ").strip().title()
    age = int(input("Enter new Student Age: ").strip())
    address = input("Enter new Student Address: ").strip().title()

    students[sid].update({
        "name": name,
        "age": age,
        "address": address
    })
    print("Student updated successfully.")

def view_student_by_id():
    sid = input("Enter Student ID: ").strip()
    info = students.get(sid)

    if not info:
        print("No student found.")
        return

    print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Address: {info['address']}")

def delete_student():
    sid = input("Enter Student ID to delete: ").strip()
    if students.pop(sid, None):
        print("Student deleted successfully.")
    else:
        print("No student found.")

# -------- Main Loop --------
while True:
    print("\n---------- Student CRUD App ----------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View Student by ID")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
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
            print("Invalid choice.")
