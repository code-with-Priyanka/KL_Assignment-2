# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area_of_circle(self):
        return math.pi * self.radius**2
    
    def perimeter_of_circle(self):
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Triangle():
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area_of_triangle(self):
        return 0.5 * self.base * self.height   
    def perimeter_of_triangle(self):
        return self.side1 + self.side2 + self.side3

while True:
    shape_type = input("Enter shape type (circle, rectangle, square, triangle): ")

    if shape_type == "circle":
        radius_of_circle = float(input("Enter radius: "))
        shape = Circle(radius_of_circle)
        print(shape.area_of_circle())
        print(shape.perimeter_of_circle())
    elif shape_type == "rectangle":
        length_of_rectangle = float(input("Enter length: "))
        width_of_rectangle = float(input("Enter width: "))
        shape = Rectangle(length_of_rectangle, width_of_rectangle)
        print(shape.area())
        print(shape.perimeter())
    elif shape_type == "square":
        side_of_square = float(input("Enter side length: "))
        shape = Square(side_of_square)
        print(shape.area())
        print(shape.perimeter())
    elif shape_type == "triangle":
        base_of_triangle = float(input("Enter base length: "))
        height_of_triangle = float(input("Enter height: "))
        side1_of_triangle = float(input("Enter side 1 length: "))
        side2_of_triangle = float(input("Enter side 2 length: "))
        side3_of_triangle = float(input("Enter side 3 length: "))
        shape = Triangle(base_of_triangle, height_of_triangle, side1_of_triangle, side2_of_triangle, side3_of_triangle)
        print(shape.area_of_triangle())
        print(shape.perimeter_of_triangle())
    else:
        print("Invalid shape type.")
        exit()

