### OOP in python: In python, we can use classes to create objects that have attributes and methods. This allows us to model real-world entities and their behaviors in our code.
# defining a class
# syntax: class <class_name>:
"""
Docstring for oop.main
class className:
statements
methods

objects: An object is an instance of a class. It is created using the class constructor and can have its own unique attributes and behaviors.

attributes: Attributes are the data stored in an object. They represent the state of the object and can be accessed and modified using methods.

methods: Methods are functions defined within a class that operate on the attributes of the class. They define the behavior of the objects created from the class.

object = className()  # creating an object of the class
object.attribute = value  # setting an attribute of the object  

"""

class Student:
    name="Naresh Bohara"
    age = 20
    def study(self):
        print(f"{self.name} is studying.")


student1 = Student()  # creating an object of the Student class
print(student1.name)  # Output: Naresh Bohara
print(student1.age)   # Output: 20
student1.study()      # Output: Naresh Bohara is studying.


### constructors: A constructor is a special method in a class that is called when an object is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.

class Student:
    def __init__(self, name, age):
        self.name = name  # initializing the name attribute
        self.age = age    # initializing the age attribute

    def study(self):
        print(f"{self.name} is studying.")

student1 = Student("Naresh Bohara", 23)  # creating an object of the Student class with name and age
print(student1.name)  # Output: Naresh Bohara
print(student1.age)   # Output: 20
student1.study()      # Output: Naresh Bohara is studying.


## self: The self parameter is a reference to the current instance of the class. It is used to access the attributes and methods of the class within its own methods. The self parameter is automatically passed to the methods when they are called on an object.

# why self is used: The self parameter is used to differentiate between instance attributes and local variables within a method. It allows us to access and modify the attributes of the object that the method is being called on.

# what happens if we don't use self: If we don't use the self parameter, we won't be able to access the attributes and methods of the class within its own methods. This will lead to errors when we try to call the methods on an object.

# how self works: When we call a method on an object, Python automatically passes the object as the first argument to the method. This is why we need to include the self parameter in the method definition to receive this argument.

# diff between self and this: In Python, we use self to refer to the current instance of the class, while in other programming languages like Java or C++, the keyword this is used for the same purpose. The main difference is that self is explicitly defined as a parameter in Python methods, while this is implicitly available in other languages.

# is self is like this in java: Yes, self in Python serves a similar purpose to this in Java. Both are used to refer to the current instance of the class and allow access to its attributes and methods. However, the syntax and usage differ between the two languages.

# what this does in java: In Java, the this keyword is used to refer to the current instance of the class. It can be used to access instance variables, call other methods, and differentiate between local variables and instance variables when they have the same name. It is also commonly used in constructors to initialize instance variables.

# is self and this is same: While self in Python and this in Java serve similar purposes in referring to the current instance of a class, they are not the same. Self is explicitly defined as a parameter in Python methods, while this is implicitly available in Java. Additionally, the syntax and usage of self and this differ between the two languages.

### 
class Counter:
    def __init__(self):
        self.count = 0  # initializing the count attribute

    def increment(self):
        self.count += 1  # incrementing the count attribute

c1 = Counter()  # creating an object of the Counter class
c2 = Counter()  # creating another object of the Counter class

c1.increment()  # incrementing the count of c1
c1.increment()  # incrementing the count of c1 again
c2.increment()  # incrementing the count of c2

print(c1.count)  # Output: 2
print(c2.count)  # Output: 1


### diff between object and variable: 
# - An object is an instance of a class that has its own unique attributes and behaviors, while a variable is a named reference to a value stored in memory. An object can have multiple attributes and methods, while a variable can only hold a single value at a time. Objects are created using classes, while variables are created using assignment statements.
