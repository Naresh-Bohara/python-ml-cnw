## Method overriding in Python
# Method overriding is a feature in object-oriented programming that allows a child class to provide a specific implementation of a method that is already defined in its parent class. When a method in a child class has the same name and signature as a method in the parent class, the child class's method will override the parent class's method. This allows the child class to modify or extend the behavior of the parent class's method while still maintaining the same interface.
# Example of method overriding in Python:
class Animal:
    def sound(self):
        print("Animal makes a sound.")
class Dog(Animal):
    def sound(self):
        super().sound()  # calling the sound method of the parent class
        print("Dog barks.")
# animal1 = Animal()
# animal1.sound()  # Output: Animal makes a sound.
dog1 = Dog()
dog1.sound()  # Output: Dog barks.

## Rules for method overriding:
# 1. The method in the child class must have the same name as the method in the parent class.
# 2. The method in the child class must have the same number of parameters as the method in the parent class.
# 3. The method in the child class can have a different implementation than the method in the parent class.
# 4. The method in the child class can call the method in the parent class using the super() function if needed.

# Method overriding is a powerful feature that allows for polymorphism, where a child class can be treated as an instance of its parent class while still providing its own specific behavior. This promotes code reusability and flexibility in object-oriented programming.

# Real world example of method overriding:
class Bank:
    def interest_rate(self):
        return 5.0  # Default interest rate for the bank
class SavingsAccount(Bank):
    def interest_rate(self):
        return 7.0  # Overriding the interest rate for savings account
class CurrentAccount(Bank):
    def interest_rate(self):
        return 3.0  # Overriding the interest rate for current account
savings_account = SavingsAccount()
current_account = CurrentAccount()  
print(f"Savings Account Interest Rate: {savings_account.interest_rate()}%")  # Output: Savings Account Interest Rate: 7.0%
print(f"Current Account Interest Rate: {current_account.interest_rate()}%")  # Output: Current Account Interest Rate: 3.0%

# another example of method overriding:
class Shape:
    def area(self):
        print("Calculating area of a shape.")
class Circle(Shape):
    def area(self):
        super().area()  # calling the area method of the parent class
        print("Calculating area of a circle.")
class Rectangle(Shape):
    def area(self):
        super().area()  # calling the area method of the parent class
        print("Calculating area of a rectangle.")
circle = Circle()
rectangle = Rectangle()
circle.area()  # Output: Calculating area of a shape. Calculating area of a circle.
rectangle.area()  # Output: Calculating area of a shape. Calculating area of a rectangle.

# Method ovrriding with constructors and parameters:
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # calling the constructor of the parent class
        self.student_id = student_id  # adding a new attribute specific to Student
    def introduce(self):
        super().introduce()  # calling the introduce method of the parent class
        print(f"My student ID is {self.student_id}.")  # adding additional behavior
student1 = Student("Naresh Bohara", "S12345")
student1.introduce()  # Output: Hello, my name is Naresh Bohara. My student ID is S12345.


