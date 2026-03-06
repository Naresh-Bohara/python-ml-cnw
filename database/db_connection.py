import mysql.connector


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naresh@123#", 
            database="school"
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None