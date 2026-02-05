# Function: block of code that perform specific task and run only when it is called.
''' syntax: 
def function_name():
        statement
        code 
        logic

function_name()

## Uses: 
- reduce repitation
- modular program
- code reuseability
'''

# Types of function in python:
# 1. Function with no parameter and no return value
# def greet():
#     print("Hello world")
# greet()

# 2. Function with parameter and no return value\
# name = parameter, "Naresh" = argument (actual value)
# def greet(name):
#     print(f"Hello {name} ")
# greet("Naresh")

# 3. Function with no parameter but return value
def greet():
    print("hello")
    return "Hello! world"
# greet()
# print(greet())
# s = greet()
# print(s)

# 4. Function with both parameter and return value
# def add(a, b):
#     s = a + b
#     return s
# print(add(1, 2))

# def greeting(name):
#     return "hello "+name
# print(greeting("Naresh"))

# def greeting(name):
#     return print(f"hello {name}")
# (greeting("Nareshzz"))


## Default argument function:
# def greet(name = "Naresh"):
#     print(f"Hello {name}")
# greet("roshan")

## keyword argument function:
# def student(name, age):
#     print(f"name: {name}, age:{age}")
# student(20, "hari")
# student(age=20, name="hari")

## varaible length argument:
# def add(*num):
#     total = 0
#     for i in num:
#         total +=i
#     return total
# print(add(1,2,3,4))
# print(add(10, 20, 30, 40, 30, 20))


# def greet(*args):
#     for i in args:
#         print(f"Hello {i}", end=" ")
#     print()
# greet("ram", "hari", "shyam")
# greet("naresh")

# def combine_names(*names):
#     result = ""
#     for name in names:
#         result += name + " "  # Add space between names
#     return result.strip()

# print(combine_names("Ram", "Shyam", "Hari"))
# # Output: Ram Shyam Hari


## keyword variable length argument:
# def student(**data):
#     for k, v in data.items():
#         print(f"k: {k}, v: {v}")
#     print()
# student(name="naresh", age=23)
# student(name="hari", age=23, add="ktm")

## nested dict create 
# def add_student(**data):
#     return data

# student = {}

# student["student1"] = add_student(name="ram", age=12)
# student["student2"] = add_student(name="hari", age=20)
# student["student3"] = add_student(name="shyam", age=23)

# print(student)


# ----------------- or ---------------------------
# def add_student(student_id, **student_data):
#     return {student_id: student_data}

# # Create the nested dictionary
# students = {}
# students.update(add_student("student1", name="ram", age=12))
# students.update(add_student("student2", name="hari", age=20))
# students.update(add_student("student3", name="shyam", age=23))

# print(students)

## accessing nested dict: 
# students = {
#     "student1": {"name": "ram", "age": 12},
#     "student2": {"name": "hari", "age": 20},
#     "student3": {"name": "shyam", "age": 23},
# }

# print(student["student1"])          # accessing entire inner dict
# print(student["student2"]["name"])  # accessing individual value


# nested dictionary and print key-value pairs 
# students = {
#     "student1": {"name": "ram", "age": 12},
#     "student2": {"name": "hari", "age": 20},
#     "student3": {"name": "shyam", "age": 23}
# }

# print("Nested Dictionary Contents:")
# print("=" * 30)

# for student_id, student_info in students.items():
#     print(f"\nStudent ID: {student_id}")
#     print("-" * 20)
#     for key, value in student_info.items():
#         print(f"  {key}: {value}")


# ----------------- or ---------------------------
# students = {
#     "student1": {"name": "ram", "age": 12},
#     "student2": {"name": "hari", "age": 20},
#     "student3": {"name": "shyam", "age": 23}
# }

# def print_nested(**students):
#     for k, v in students.items():
#         print(f"k: {k}, v: {v}")
#         # If v is a dictionary, show its k,v too
#         if isinstance(v, dict):
#             for inner_k, inner_v in v.items():
#                 print(f"  inner_k: {inner_k}, inner_v: {inner_v}")
#         print()

# # Call it
# print_nested(
#     student1={"name": "ram", "age": 12},
#     student2={"name": "hari", "age": 20},
#     student3={"name": "shyam", "age": 23}
# )

# ----------------- or ---------------------------
students = {
    "student1": {"name": "ram", "age": 12},
    "student2": {"name": "hari", "age": 20},
    "student3": {"name": "shyam", "age": 23}
}

# Just like your k, v example but nested
for k1, v1 in students.items():  # First level: student1, student2, etc.
    print(f"\nOuter Key: {k1}")
    print(f"Outer Value (full dict): {v1}")
    
    for k2, v2 in v1.items():  # Second level: name, age
        print(f"{k2}: {v2}")
        # print(f"  Inner Value: {v2}")

