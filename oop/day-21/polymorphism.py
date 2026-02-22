## polymorphism: many forms
# Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as instances of the same class through a common interface. It enables a single function or method to work with different types of objects, providing flexibility and extensibility in code design. Polymorphism can be achieved through method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class. This allows for dynamic method dispatch, where the appropriate method is called based on the actual type of the object at runtime. Polymorphism promotes code reusability and makes it easier to maintain and extend code by allowing new classes to be added without modifying existing code.
# - achieved via method overriding
# - allows objects of different classes to be treated as instances of the same class through a common interface
# - promotes code reusability and flexibility in code design
# - enables dynamic method dispatch based on the actual type of the object at runtime

# Example of polymorphism in Python:
class Shape:
    def area(self):
        print("Calculating area of a shape.")
class Circle(Shape):
    def area(self, radius):
        super().area()  # calling the area method of the parent class
        print(f"Calculating area of a circle with radius {radius}. Area = {3.14 * radius * radius}")
class Rectangle(Shape):
    def area(self, length, width):
        super().area()  # calling the area method of the parent class
        print(f"Calculating area of a rectangle with length {length} and width {width}. Area = {length * width}")
circle = Circle()
rectangle = Rectangle() 
circle.area(5)  # Output: Calculating area of a shape. Calculating area of a circle with radius 5. Area = 78.5
rectangle.area(4, 6)  # Output: Calculating area of a shape. Calculating area of a rectangle with length 4 and width 6. Area = 24

# another example of polymorphism:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self, name):  # Different parameter!
        print(f"{name} says Woof!")

class Cat(Animal):
    def speak(self, name, volume):  # Different parameters!
        print(f"{name} says Meow at {volume}")

# ❌ Can't use polymorphism!
animals = [Dog(), Cat()]

for animal in animals:
    # What parameters to pass? Different for each!
    animal.speak()  # ERROR!
    animal.speak("Buddy")  # Cat would fail!
    animal.speak("Buddy", "loud")  # Dog would fail!

### true polymorphism with a common interface
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):  # Same parameters (none)
        print("Woof!")

class Cat(Animal):
    def speak(self):  # Same parameters (none)
        print("Meow!")

# ✅ TRUE POLYMORPHISM!
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()  # Same call works for all!
    
# Output:
# Woof!
# Meow!