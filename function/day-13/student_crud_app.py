# ------------------ Student CRUD App (Assignment) ------------------

"""
---------------- Student CRUD App ----------------
### Features:
- add, view, view by id, update, delete student records
- update specific student field or all fields.
- email validation, ends with @gmail.com
- age validation, between 5 and 105
- arguments pasing for crud operations
- use of match-case
"""

students ={}

def validate_text_input(value, field_name, min_chars=1):
    value = value.strip()
    if not value:
        print(f"Validation Failed: {field_name} can't be empty.")
        return None
    if len(value) < min_chars:
        print(f"Validation Failed: {field_name} must be at least of {min_chars } chars.")
        return None
    return value

def validate_email(email):
    email = email.strip().lower()
    if not email.endswith("@gmail.com"):
        print("Validation Failed: Enter valid email, ends with @gmail.com")
        return None
    return email

def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        print("Validation Failed: Age must be a number.")
        return None
    if not (5 <= age <= 105):
        print("Validation Failed: Age must be between 5 and 105.")
        return None
    return age

def add_student(sid, name, age, email, address):
    # validate all input fileds
    sid = validate_text_input(sid, "Student Id", min_chars=1)
    name = validate_text_input(name, "Student Name", min_chars=3)
    age = validate_age(age)
    email = validate_email(email)
    address = validate_text_input(address, "Student Address", min_chars=3)

    # check if any validation failed
    if None in (sid, name, age, email, address):
        print("Failed to add Student. Please fill the fields clearly.")
        return
    
    # check if student is already exist
    if sid in students:
        print(f"Student Id {sid} already exists.")
        return
    
    # add student to dict
    students[sid] = {
        "name": name.title(),
        "age": age,
        "email": email,
        "address": address.title()
    }

    print(f"Student {name} added successfully.")
    # print(students)
def view_student():
    if not students:
        print("No Students Found.")
        return
    
    print("----- All Students: -----")
    for sid, info in students.items():
        print(f"Id: {sid}, Name: {info['name']}, Age: {info['age']}, Email: {info['email']},  Address: {info['address']}")

def view_student_by_id(sid):
    sid = validate_text_input(sid, "Student Id", min_chars=1)
    if not sid:
        return
    
    student = students.get(sid)
    if student:
        print(f"----- Student's detail for id: {sid} -----")
        print(f"Student Name : {student['name']}")
        print(f"Student Age : {student['age']}")
        print(f"Student Email : {student['email']}")
        print(f"Student Address : {student['address']}")
    else:
        print(f"No Student Found for id: {sid}")

# update student by id
def update_student(sid):
    sid = validate_text_input(sid, "Student Id", min_chars=1)
    if not sid:
        return
    if sid not in students:
        print(f"Student id: {sid} not Found.")
        return
    
    student = students[sid]
    print(f"Current Name: {student['name']}")
    name = input("New Name (press enter for kepping same): ").strip()
    if name:
        name = validate_text_input(name, "Student Name", min_chars=3)
        if name:
            student['name'] = name.title()


    print(f"Current Age: {student['age']}")
    age = input("New Age (press enter for kepping same): ").strip()
    if age:
        age = validate_age(age)
        if age:
            student['age'] = age
    
    print(f"Current Email: {student['email']}")
    email = input("New Email (press enter for kepping same): ").strip()
    if email:
        email = validate_email(email)
        if email:
            student['email'] = email

    print(f"Current Address: {student['address']}")
    address = input("New Address (press enter for keeping same): ").strip()
    if address:
        address = validate_text_input(address, "Student Address", min_chars=3)
        if address:
            student['address'] = address.title()
    print(f"Student {sid} updated successfully.")

def delete_student(sid):
    sid = validate_text_input(sid, "Student Id", min_chars=1)
    if not sid:
        return
    if sid in students:
        del students[sid]
        print(f"Student with id: {sid} deleted successfully.")
    else:
        print(f"Student with {sid} Not Found.")

def search_student(search_term):
    if not search_term:
        print("Please enter a search term")
        return
    
    search_term = search_term.lower()
    found = False
    
    for sid, info in students.items():
        if(search_term in sid.lower() or 
           search_term in info['name'].lower() or 
           search_term in info['address'].lower() or 
           search_term in info['email']):
            print(f"""Student Found:
                  Student Name: {info['name']}
                  Student Email: {info['email']}
                  Student Age: {info['age']}
                  Student Address: {info['address']}
""")
            found = True
    if not found:
            print(f"No student found with '{search_term}' ")

def main():
    while True:
        print("""
----------------------- Student CRUD App ------------------------------
              1. Add Student
              2. View all Students
              3. View Student by Id
              4. Update Student
              5. Delete Student
              6. Search Student
              7. Exit
""")
        try:
            choice = int(input("Please Enter your choice (1-7) what you want to perform: "))
        except ValueError:
            print("Please enter a number only.")
            continue
        match choice:
            case 1:
                print("----- Add New Student -----")
                sid = input("Student Id: ")
                name = input("Student Name: ")
                age = input("Student Age: ")
                email = input("Student Email: ")
                address = input("Student Address: ")
                add_student(sid=sid, name=name, age=age, email=email, address=address)
            
            case 2:
                view_student()
            
            case 3:
                print("----- View Student by Id -----")
                sid = input("Please Enter Student Id: ")
                view_student_by_id(sid)

            case 4:
                print("----- Update Student -----")
                sid = input("Please enter Student Id: ")
                update_student(sid)

            case 5:
                print("----- Delete Student -----")
                sid = input("Please enter Student Id: ")
                delete_student(sid)

            case 6:
                print("----- Search Student -----")
                search_term = input("Search by Id, Name, Email, or Address: ")
                search_student(search_term)

            case 7:
                print("Exiting...")
                break

            case _:
                print("Invalid choice. Try again.")

main()
