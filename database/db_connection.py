import mysql.connector

def db_connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naresh@123#", 
            database="school"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
    