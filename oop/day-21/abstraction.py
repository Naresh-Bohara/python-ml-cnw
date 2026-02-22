## abstraction
## hiding the implementation details and showing only the functionality to the user
## abstraction is achieved via abstract classes and interfaces

## abstract class: An abstract class is a class that cannot be instantiated and is meant to be subclassed. It can contain abstract methods, which are methods that are declared but not implemented in the abstract class. Subclasses of the abstract class must provide an implementation for the abstract methods. Abstract classes are used to define a common interface for a group of related classes and to enforce a certain structure on the subclasses.

## interface: An interface is a collection of abstract methods that define a contract for classes that implement the interface. An interface specifies what methods a class must implement, but does not provide any implementation for those methods. In Python, we can use abstract base classes (ABCs) to create interfaces. A class that implements an interface must provide an implementation for all the methods defined in the interface. Interfaces are used to achieve polymorphism and to allow different classes to be treated as instances of the same type based on the common interface they implement.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")

car = Car()
car.start_engine()  # Output: Car engine started.
motorcycle = Motorcycle()
motorcycle.start_engine()  # Output: Motorcycle engine started.


### Eg of abstraction with abstract classes and interfaces:
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius 
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width 
circle = Circle(5)
print(f"Area of circle: {circle.area()}")  # Output: Area of circle: 78.5
rectangle = Rectangle(4, 6)
print(f"Area of rectangle: {rectangle.area()}")  # Output: Area of rectangle: 24


### Another example of abstraction with interfaces:
