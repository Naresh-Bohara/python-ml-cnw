# Exception handling in Python allows you to manage errors gracefully without crashing your program. You can use try-except blocks to catch and handle exceptions. Here's an example of how to use exception handling in Python:

# error eg: 
# print(10 / 0)  # This will raise a ZeroDivisionError

# Types of errors:
# 1. SyntaxError: Raised when there is a syntax error in the code.
# 2. NameError: Raised when a variable is not defined.
# 3. TypeError: Raised when an operation is performed on an inappropriate type.
# 4. ValueError: Raised when a function receives an argument of the right type but an inappropriate value.
# 5. ZeroDivisionError: Raised when division by zero is attempted.
# 6. FileNotFoundError: Raised when trying to open a file that does not exist.
# 7. IndexError: Raised when trying to access an index that is out of range.
# 8. KeyError: Raised when trying to access a key that does not exist in a dictionary.
# 9. AttributeError: Raised when an attribute reference or assignment fails.
# 10. ImportError: Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
# 11. IOError: Raised when an I/O operation fails.
# 12. RuntimeError: Raised when an error is detected that doesn't fall in any of the other categories.
# 13. LogicError: Raised when there is a logical error in the code, which may not necessarily raise an exception but leads to incorrect behavior.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution completed.")


# You can also catch multiple exceptions:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("The result is:", result)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)


# You can raise your own exceptions using the raise statement:
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Valid age:", age)

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as ve:
    print("Error:", ve)


# CUSTOM EXCEPTION
class NegativeAgeError(Exception):
    """Custom exception for negative age values."""
    pass
def validate_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    else:
        print("Valid age:", age) 
try:
    age = int(input("Enter your age: "))
    validate_age(age)  
except NegativeAgeError as nae:
    print("Error:", nae)
