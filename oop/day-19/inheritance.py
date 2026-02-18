### inheritance: Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

# -child class can override the methods of the parent class to provide specific implementations.
# -child class can also add new attributes and methods to enhance the functionality of the parent class
# syntax: class ChildClass(ParentClass):

# Example of inheritance in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") 

    def greet(self):
        print(f"Hi, I am {self.name}. Nice to meet you!")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # calling the constructor of the parent class
        self.student_id = student_id  # adding a new attribute specific to Student

    def introduce(self):
        super().introduce()  # calling the introduce method of the parent class
        print(f"My student ID is {self.student_id}.")  # adding additional behavior

student1 = Student("Naresh Bohara", 23, "S12345")
student1.introduce()    # Output: Hello, my name is Naresh Bohara and I am 23 years old. My student ID is S12345.
student1.greet()        # Output: Hi, I am Naresh Bohara. Nice to meet you!



### inheritance with constructors: When a child class inherits from a parent class, it can override the constructor of the parent class to provide its own initialization logic. However, if the child class wants to use the constructor of the parent class, it can call it using the super() function. The super() function allows the child class to access the methods and attributes of the parent class, including the constructor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # calling the constructor of the parent class
        self.student_id = student_id  # adding a new attribute specific to Student  
    def introduce(self):
        super().introduce()  # calling the introduce method of the parent class
        print(f"My student ID is {self.student_id}.")  # adding additional behavior
student1 = Student("Naresh Bohara", 23, "S12345")
student1.introduce()    # Output: Hello, my name is Naresh Bohara and I am 23 years old. My student ID is S12345.


### super keyword: The super() function is used to call a method from the parent class in a child class. It allows the child class to access and use the methods and attributes of the parent class without explicitly naming it. This is particularly useful when you want to extend or modify the behavior of a method in the child class while still retaining the functionality of the parent class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # calling the constructor of the parent class
        self.student_id = student_id  # adding a new attribute specific to Student  
    def introduce(self):
        super().introduce()  # calling the introduce method of the parent class
        print(f"My student ID is {self.student_id}.")  # adding additional behavior 
student1 = Student("Naresh Bohara", 23, "S12345")
student1.introduce()    # Output: Hello, my name is Naresh Bohara and I am 23 years old. My student ID is S12345.