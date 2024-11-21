from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
    
    @abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * self.a + 2 * self.b


circle = Circle(3)
print(f"Area: {circle.area()}; Perimeter: {circle.perimeter()}")

rectangle = Rectangle(2, 2)
print(f"Area: {rectangle.area()}; Perimeter: {rectangle.perimeter()}")


shape = Shape()
print(shape)
