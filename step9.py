# 9. Abstract Classes and Methods

# Assignment:

# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method with no implementation

# Concrete Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# --- Testing ---
rect = Rectangle(10, 5)
print(f"🧮 Area of Rectangle: {rect.area()}")
