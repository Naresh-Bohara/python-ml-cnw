### Inheritance types:
# 1. Single Inheritance: In single inheritance, a child class inherits from a single parent class. This is the most basic form of inheritance and allows the child class to access the properties and behaviors of the parent class.
# Exxample of single inheritance: A -> B
class Animal:
    def eat(self):
        print("This animal eats food.")
class Dog(Animal):
    def bark(self):
        print("The dog barks.")

dog1 = Dog()
dog1.eat()  # Output: This animal eats food.
dog1.bark()  # Output: The dog barks.

# 2. Multilevel Inheritance: In multilevel inheritance, a child class inherits from a parent class, and then another child class inherits from that child class. This creates a chain of inheritance where each class can access the properties and behaviors of its parent classes.
# Example of multilevel inheritance: A -> B -> C
class Grandfather:
    def land(self):
        print("Grandfather owns land.")
class Father(Grandfather):
    def house(self):
        print("Father owns a house.")
class Son(Father):
    def car(self):
        print("Son owns a car.")
son1 = Son()
son1.land()   # Output: Grandfather owns land.
son1.house()  # Output: Father owns a house.
son1.car()    # Output: Son owns a car.

# 3. Multiple Inheritance: In multiple inheritance, a child class can inherit from more than one parent class. This allows the child class to combine the properties and behaviors of multiple parent classes. However, it can also lead to ambiguity if there are conflicting attributes or methods in the parent classes.
# Example of multiple inheritance:A -> B, A -> C
class Mother:
    def cooking(self):
        print("Mother is cooking.")
class Father:
    def working(self):
        print("Father is working.")
class Child(Mother, Father):
    def playing(self):
        print("Child is playing.")
child1 = Child()
child1.cooking()  # Output: Mother is cooking.  
child1.working()  # Output: Father is working.
child1.playing()  # Output: Child is playing.


# 4. Hierarchical Inheritance: In hierarchical inheritance, multiple child classes inherit from a single parent class. This allows each child class to have its own unique properties and behaviors while still sharing the common features of the parent class.
# Example of hierarchical inheritance: A -> B, A -> C, A -> D
class Vehicle:
    def start(self):
        print("Vehicle is starting.")
    def engine(self):
        print("Vehicle has an engine.")
    def stop(self):
        print("Vehicle is stopping.")
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels.")
class Bus(Vehicle):
    def wheels(self):
        print("Bus has 6 wheels.")
car1 = Car()
bike1 = Bike()
bus1 = Bus()
car1.start()  # Output: Vehicle is starting.
car1.engine() # Output: Vehicle has an engine.
car1.stop()   # Output: Vehicle is stopping.
car1.wheels() # Output: Car has 4 wheels.
bike1.start()  # Output: Vehicle is starting.
bike1.engine() # Output: Vehicle has an engine.
bike1.stop()   # Output: Vehicle is stopping.
bike1.wheels() # Output: Bike has 2 wheels.
bus1.start()  # Output: Vehicle is starting.
bus1.engine() # Output: Vehicle has an engine.
bus1.stop()   # Output: Vehicle is stopping.
bus1.wheels() # Output: Bus has 6 wheels.


# 5. Hybrid Inheritance: Hybrid inheritance is a combination of two or more types of inheritance. It allows for more complex relationships between classes and can be used to model real-world scenarios more accurately. However, it can also lead to increased complexity and potential issues with method resolution order (MRO) if not designed carefully.
# Example of hybrid inheritance: A -> B, A -> C, B -> D
class A:
    def method_a(self):
        print("Method A from class A.")
class B(A):
    def method_b(self):
        print("Method B from class B.")
class C(A):
    def method_c(self):
        print("Method C from class C.")
class D(B, C):
    def method_d(self):
        print("Method D from class D.")
d1 = D()
d1.method_a()  # Output: Method A from class A.
d1.method_b()  # Output: Method B from class B.
d1.method_c()  # Output: Method C from class C.
d1.method_d()  # Output: Method D from class D.




