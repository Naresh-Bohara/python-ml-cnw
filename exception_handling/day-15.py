# else in exception handling is used to specify a block of code that will be executed if no exceptions are raised in the try block. It is optional and can be used to perform actions that should only occur when the try block executes successfully.

# try:
#     # Code that may raise an exception
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("The result is:", result)
# except (ValueError, ZeroDivisionError) as e:
#     # Code to handle the exception
#     print("Error:", e)
# else:
#     # Code to execute if no exceptions were raised
#     print("No exceptions were raised. The operation was successful.")   

# finally in exception handling is used to define a block of code that will always be executed, regardless of whether an exception was raised or not. It is typically used for cleanup actions, such as closing files or releasing resources.

# try:
#     file = open('non_existent_file.txt', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: File not found.")
# finally:
#     print("Execution completed.")
#     # Code that will always execute, regardless of exceptions   

# type error:
# try:
#     result = '2' + 2
#     print("The result is:", result)
# except TypeError as te:
#     print("Type Error:", te)

# ValueError:
# try:
#     num = int("abc")
#     print("The number is:", num)    
# except ValueError as ve:
#     print("Value Error:", ve)

# NameError:
# try:
#     print(undefined_variable)
# except NameError as ne:
#     print("Name Error:", ne)

    
# IndexError:
# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError as ie:
#     print("Index Error:", ie)

#  import error:
try:
    import naresh_bohara_module
except ImportError as ie:
    print("Import Error:", ie)
