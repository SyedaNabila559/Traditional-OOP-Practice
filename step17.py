# 17. Class Decorators

# Assignment:

# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Class decorator to add a greet method
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

# Applying the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, my name is {self.name}."

# --- Testing the class decorator ---
person = Person("Alice")
print(person.introduce())  # Original method
print(person.greet())  # Added by the decorator
