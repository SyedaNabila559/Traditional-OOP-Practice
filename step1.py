# 1. Using self

# Assignment:

# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name      # Using 'self' to assign the name
        self.marks = marks    # Using 'self' to assign the marks
        print("Constructor Called!")  # Debug message to check if constructor is called

    def display(self):
        print(f"Student Name: {self.name}")  # This should print the name
        print(f"Marks: {self.marks}")  # This should print the marks

# Create an instance of the Student class
student1 = Student("Alice", 92)

# Calling the display method to show details
student1.display()