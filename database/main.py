import mysql.connector

# step 1: Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naresh@123#",
    database="school"
)
if conn.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# step 2: Create a cursor object to interact with the database
cursor = conn.cursor()

while True:
    print("\n 1) Insert Record")
    print(" 2) Update Record")
    print(" 3) Delete Record")
    print(" 4) Display Records")
    print(" 5) Exit")

    choice = int(input("Enter your choice: ")) 
    match choice:
        case 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            city = input("Enter city: ")
            sql = "INSERT INTO students (name, age, city) VALUES (%s, %s, %s)"
            values = (name, age, city)
            cursor.execute(sql, values)
            conn.commit()
            print("Record inserted successfully")
        case 2:
            student_id = int(input("Enter student ID to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_city = input("Enter new city: ")
            sql = "UPDATE students SET name = %s, age = %s, city = %s WHERE id = %s"
            values = (new_name, new_age, new_city, student_id)
            cursor.execute(sql, values)
            conn.commit()   
            print("Record updated successfully")
        case 3:
            student_id = int(input("Enter student ID to delete: "))
            sql = "DELETE FROM students WHERE id = %s"
            values = (student_id,)
            cursor.execute(sql, values)
            conn.commit()
            print("Record deleted successfully")
        case 4:
            sql = "SELECT * FROM students"
            cursor.execute(sql)
            records = cursor.fetchall()
            for record in records:
                print(record)
        case 5:
            print("Exiting...") 
            break
        case _:
            print("Invalid choice. Please try again.")
# step 3: Close the cursor and connection
cursor.close()
conn.close()

