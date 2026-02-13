# Student CRUD Application

def create_student():
    try:
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: ").strip())
        marks = float(input("Enter Student Marks: ").strip())

        student_id = 1

        # Check last ID
        try:
            with open('exception_handling/students.txt', 'r') as file:
                lines = file.readlines()
                if lines:
                    last_id = int(lines[-1].split(',')[0])
                    student_id = last_id + 1
        except FileNotFoundError:
            # File doesn't exist → first student
            student_id = 1

        # Now write student
        with open('exception_handling/students.txt', 'a') as file:
            file.write(f"{student_id},{name},{age},{marks}\n")

    except ValueError:
        print("Invalid input. Please enter correct data types.")
    else:
        print("Student record created successfully.")

def view_student():
    try:
        with open('exception_handling/students.txt', 'r') as file:
            students = file.read()
            if not students:
                print("No student records found.")
                return
            print("Student Records:")
            print(students)
    except FileNotFoundError:
        print("No student records found. Please create a student first.")

def search_student():
    target_id = input("Enter Student ID to Search: ").strip()
    try:
        with open('exception_handling/students.txt', 'r') as file:
            found = False
            for line in file:
                student_id, name, age, marks = line.strip().split(',')
                if student_id == target_id:
                    print(f"Student Found: ID={student_id}, Name={name}, Age={age}, Marks={marks}")
                    found = True
                    break
            if not found:
                print("Student not found.")
    except FileNotFoundError:
        print("No student records found. Please create a student first.")

def delete_student():
    target_id = input("Enter Student ID to Delete: ").strip()
    try:
        with open('exception_handling/students.txt', 'r') as file:
            students = file.readlines()
        
        with open('exception_handling/students.txt', 'w') as file:
            found = False
            for line in students:
                student_id, name, age, marks = line.strip().split(',')
                if student_id == target_id:
                    found = True
                    continue  # Skip writing this line to delete
                file.write(line)
            if found:
                print("Student record deleted successfully.")
            else:
                print("Student not found.")
    except FileNotFoundError:
        print("No student records found. Please create a student first.")

def update_student():
    target_id = input("Enter Student ID to Update: ").strip()
    try:
        with open('exception_handling/students.txt', 'r') as file:
            students = file.readlines()
        
        with open('exception_handling/students.txt', 'w') as file:
            found = False
            for line in students:
                student_id, name, age, marks = line.strip().split(',')
                if student_id == target_id:
                    found = True
                    print(f"Current Record: ID={student_id}, Name={name}, Age={age}, Marks={marks}")
                    new_name = input("Enter new name (leave blank to keep current): ").strip() or name
                    new_age = input("Enter new age (leave blank to keep current): ").strip() or age
                    new_marks = input("Enter new marks (leave blank to keep current): ").strip() or marks
                    file.write(f"{student_id},{new_name},{new_age},{new_marks}\n")
                else:
                    file.write(line)
            if found:
                print("Student record updated successfully.")
            else:
                print("Student not found.")
    except FileNotFoundError:
        print("No student records found. Please create a student first.")

def main():
    while True:
        print("""
----------------------- Student CRUD App ------------------------------
1. Create Student
2. View Student
3. Search Student
4. Delete Student
5. Update Student
6. Exit
""")
        choice = input("Please Enter your choice (1-6) what you want to perform: ")
        match choice:
            case '1':
                print("----- Create Student -----")
                create_student()
                
            case '2':
                print("----- view Student -----")
                view_student()
            case '3':
                print("----- Search Student -----")
                search_student()
            case '4':
                print("----- Delete Student -----")
                delete_student()
            
            case '5':
                print("------------ Update Student ------------")
                update_student()
            case '6':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Try again.")


main()