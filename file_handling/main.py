# File Handing: file handling is the process of reading and writing files in a programming language. In Python, we can use the built-in open() function to open a file and perform various operations on it, such as reading, writing, and appending. We can also use the with statement to ensure that the file is properly closed after we are done with it. File handling is an essential part of programming, as it allows us to store and retrieve data from files, which can be used for various purposes such as data analysis, logging, and configuration management.

# -> File handline allows us ti manipulate files, such as creating, reading, writing, and deleting files.

# Steps to perform file handling in Python:
# 1. Open the file using the open() function.   
# 2. Perform the desired operations on the file (e.g., read, write, append).
# 3. Close the file using the close() method or by using a with statement to ensure it is properly closed.

# syntax: 
# file = open('filename', 'mode')

# Modes:
# 'r' - Read mode (default): Opens a file for reading. If the file does not exist, it raises a FileNotFoundError.
# 'w' - Write mode: Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# 'a' - Append mode: Opens a file for appending. If the file already
# exists, it appends the new data to the end of the file. If the file does not exist, it creates a new file.
# 'x' - Exclusive creation mode: Opens a file for exclusive creation. If the file already exists, it raises a FileExistsError. If the file does not exist, it creates a new file.
# 'b' - Binary mode: Opens a file in binary mode. This is used for non-text files, such as images or videos.
# 't' - Text mode (default): Opens a file in text mode. This is used for text files.

# Example: 
# 1. write mode: 'w'
file = open('file_handling/hello.txt', 'w')
file.write("Hello, World!")
file.close()

# 2. read mode: 'r'
file = open('file_handling/hello.txt', 'r')
data = file.read()
print(data)
file.close()

# 3. append mode: 'a'
file = open('file_handling/hello.txt', 'a')
file.write("\nWelcome to File Handling in Python.")
file.close()

# 4. read and write mode: 'r+'
'''
- file must already exist to open in 'r+' mode.
- can read and write both.
'''
file = open('file_handling/hello.txt', 'r+')
data = file.read()
print(data)
file.write("\nThis line was added using 'r+' mode.")
file.close()

# 5. write and read mode: 'w+'
'''
- file will be created if it does not exist, and truncated to zero length if it does exist.
- can read and write both.
'''
file = open('file_handling/hello.txt', 'w+')
file.write("This file was created using 'w+' mode.")
file.seek(0)  # Move the file pointer to the beginning of the file
data = file.read()
print(data)
file.close()

# 6. append and read mode: 'a+'
'''
- file will be created if it does not exist.
- can read and write both, but writing will always append to the end of the file.
'''
file = open('file_handling/hello.txt', 'a+')
file.write("\nThis line was added using 'a+' mode.")
file.seek(0)  # Move the file pointer to the beginning of the file
data = file.read()
print(data)
file.close()

# another way of opening and closing file using with statement:
with open('file_handling/hello.txt', 'r') as file:
    data = file.read()
    print("--------- Data read using with statement: ----------")
    print(data)


# saving user input to a file:
name = input("Enter your name: ")
age = input("Enter your age: ")
with open('file_handling/user_data.txt', 'w') as file:
    file.write(f"Name: {name}\nAge: {age}\n")
print("User data saved to 'user_data.txt'")