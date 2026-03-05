import mysql.connector
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