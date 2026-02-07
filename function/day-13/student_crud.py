# 

students ={}
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
    print(students)

def view_students():
    if not students:
        print("No students found.")
        return
    print("Student List:")
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Address: {info['address']}")

def update_student():
    sid = input("Enter Student ID to update: ").strip()
    if sid in students:
        name = input("Enter new Student Name: ").strip().title()
        age = int(input("Enter new Student Age: ").strip())
        address = input("Enter new Student Address: ").strip().title()

        students[sid] = {
            "name": name,
            "age": age,
            "address": address
        }
        print(f"Student with ID {sid} updated successfully.")
    else:
        print(f"No student found with ID {sid}.")

def view_student_by_id():
    sid = input("Enter Student ID to view: ").strip()
    if sid in students:
        info = students[sid]
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Address: {info['address']}")
    else:
        print(f"No student found with ID {sid}.")

def delete_student():
    sid = input("Enter Student ID to delete: ").strip()
    if sid in students:
        del students[sid]
        print(f"Student with ID {sid} deleted successfully.")
    else:
        print(f"No student found with ID {sid}.")

while True:
    print(" \n---------- Student CRUD App ---------- ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View Student by ID")
    print("6. Exit")

    choice = int(input("Enter your choice (1-5): "))
    print()
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        view_student_by_id()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    