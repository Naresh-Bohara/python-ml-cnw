### access control: Access control is a mechanism that restricts access to certain attributes and methods of a class. In Python, we can use the following conventions to indicate the intended level of access for class members:
# public: Public members are accessible from anywhere, both inside and outside the class. They are defined without any special prefix. For example:
# class MyClass:
#     public_attribute = "I am public"
# private: Private members are intended to be accessed only within the class. They are defined with a double underscore prefix. For example:
# class MyClass:
#     __private_attribute = "I am private
# protected: Protected members are intended to be accessed within the class and its subclasses. They are defined with a single underscore prefix. For example:
# class MyClass:
#     _protected_attribute = "I am protected"
# It is important to note that these conventions are not enforced by the Python interpreter, and they are only a way to indicate the intended level of access. In practice, all members of a class can be accessed from outside the class, but it is considered good practice to follow these conventions to indicate the intended usage of the class members.


# class Student:
#     def __init__(self, name, age):
#         self.name = name  # public attribute
#         self._age = age   # protected attribute
#         self.__grade = "A"  # private attribute

#     def study(self):
#         print(f"{self.name} is studying.")
# student1 = Student("Naresh Bohara", 23)
# print(student1.name)  # Output: Naresh Bohara (public attribute)
# print(student1._age)  # Output: 23 (protected attribute, but can be accessed)
# # print(student1.__grade)  # This will raise an AttributeError (private attribute)


# protected attribute can be accessed but it is not recommended to access it from outside the class. It is intended to be accessed within the class and its subclasses. Private attributes, on the other hand, cannot be accessed directly from outside the class and are intended to be used only within the class.

## inheritance eg of access control

class Student:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self._age = age   # protected attribute
        self.__grade = "A"  # private attribute

    def study(self):
        print(f"{self.name} is studying.")

class GraduateStudent(Student):
    def display_info(self):
        print(f"Name: {self.name}")  # Accessing public attribute
        print(f"Age: {self._age}")   # Accessing protected attribute
        # print(f"Grade: {self.__grade}")  # This will raise an AttributeError (private attribute)
graduate_student = GraduateStudent("Naresh Bohara", 23)
graduate_student.display_info()  # Output: Name: Naresh Bohara, Age:
graduate_student.study()  # Output: Naresh Bohara is studying.


## protected example:
class Student:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self._age = age   # protected attribute

    def study(self):
        print(f"{self.name} is studying.")

    # protected method eg
    def _display_age(self):
        print(f"{self.name} is {self._age} years old.")

class GraduateStudent(Student):
    def display_info(self):
        print(f"Name: {self.name}")  # Accessing public attribute
        self._display_age()  # Accessing protected method

graduate_student = GraduateStudent("Naresh Bohara", 23)
graduate_student.display_info()  # Output: Name: Naresh Bohara, Naresh Bohara is 23 years old.


## private example:
class Student:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age   # private attribute

    def study(self):
        print(f"{self.name} is studying.")

    # private method eg
    def __display_age(self):
        print(f"{self.name} is {self.__age} years old.")

class GraduateStudent(Student):
    def display_info(self):
        print(f"Name: {self.name}")  # Accessing public attribute
        # self.__display_age()  # This will raise an AttributeError (private method)
graduate_student = GraduateStudent("Naresh Bohara", 23)
graduate_student.display_info()  # Output: Name: Naresh Bohara


