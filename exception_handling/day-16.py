# Student CRUD Application

def create_student():
    try:
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: ").strip())
        marks = float(input("Enter Student Marks: ").strip())
        
        with open('exception_handling/students.txt', 'a') as file:
            file.write(f"{name},{age},{marks}\n")
    except ValueError as ve:
        print("Invalid input. Please enter correct data types.")
    except FileNotFoundError as fnfe:
        print("File not found error:", fnfe)
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
    search_name = input("Enter Student Name to Search: ").strip()
    try:
        with open('exception_handling/students.txt', 'r') as file:
            found = False
            for line in file:
                name, age, marks = line.strip().split(',')
                if name.lower() == search_name.lower():
                    print(f"Student Found: Name: {name}, Age: {age}, Marks: {marks}")
                    found = True
                    break
            if not found:
                print("Student not found.")
    except FileNotFoundError:
        print("No student records found. Please create a student first.")

def delete_student():
    target_name = input("Enter Student Name to Delete: ").strip()
    try:
        with open('exception_handling/students.txt', 'r') as file:
            students = file.readlines()
        
        with open('exception_handling/students.txt', 'w') as file:
            found = False
            for line in students:
                name, age, marks = line.strip().split(',')
                if name.lower() != target_name.lower():
                    file.write(line)
                else:
                    found = True
            if found:
                print("Student record deleted successfully.")
            else:
                print("Student not found.")
    except FileNotFoundError:
        print("No student records found. Please create a student first.")

def update_student():
    target_name = input("Enter Student Name to Update: ").strip()
    try:
        with open('exception_handling/students.txt', 'r') as file:
            students = file.readlines()
        
        with open('exception_handling/students.txt', 'w') as file:
            found = False
            for line in students:
                name, age, marks = line.strip().split(',')
                if name.lower() == target_name.lower():
                    new_name = input("Enter new Name: ").strip()
                    new_age = input("Enter new Age: ").strip()
                    new_marks = input("Enter new Marks: ").strip()
                    file.write(f"{new_name},{new_age},{new_marks}\n")
                    found = True
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
5. Exit
""")
        choice = input("Please Enter your choice (1-5) what you want to perform: ")
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