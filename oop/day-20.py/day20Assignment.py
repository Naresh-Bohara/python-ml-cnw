### ---------------- Assignment day-20 ----------------###

# 1. create a base class Shape with method area(a,b).
# override it in class Rectangle to calculate and print area

class Shape:
    def area(self, a, b):
        print("Base Shape area (not implemented)")

class Rectangle(Shape):
    def area(self, a, b):
        rect_area = a * b
        print(f"Rectangle area (length={a}, width={b}) = {rect_area}")

# Example usage
rect = Rectangle()
rect.area(5, 3)   # Output: Rectangle area (length=5, width=3) = 15

# 2. create a base class Triangle with method area(b,h).
# override it in class RightTriangle to calculate and print area

class shape:
    def volume(self, x, y, z):
        print("Base shape volume (not implemented)")

class Cuboid(shape):
    def volume(self, x, y, z):
        cuboid_vol = x * y * z
        print(f"Cuboid volume (length={x}, width={y}, height={z}) = {cuboid_vol}")

# Example usage
c = Cuboid()
c.volume(2, 3, 4)   # Output: Cuboid volume (length=2, width=3, height=4) = 24


#3. create a class shape with method volume(x,y,z).
# override it in class Cuboid to calculate and print volume
# Task 1
class Shape:
    def area(self, a, b):
        print("Base Shape area (not implemented)")

class Rectangle(Shape):
    def area(self, a, b):
        print(f"Rectangle area = {a * b}")

# Task 2
class Triangle:
    def area(self, b, h):
        print("Base Triangle area (not implemented)")

class RightTriangle(Triangle):
    def area(self, b, h):
        print(f"RightTriangle area = {0.5 * b * h}")

# Task 3
class shape:
    def volume(self, x, y, z):
        print("Base shape volume (not implemented)")

class Cuboid(shape):
    def volume(self, x, y, z):
        print(f"Cuboid volume = {x * y * z}")

# Testing
r = Rectangle()
r.area(5, 3)

t = RightTriangle()
t.area(4, 6)

c = Cuboid()
c.volume(2, 3, 4)