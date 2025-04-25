# 10. Instance Methods

# Assignment:

# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name       # Instance variable
        self.breed = breed     # Instance variable

    def bark(self):
        print(f"🐶 {self.name} says: Woof woof!")

# --- Testing the Dog class ---
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

dog1.bark()
dog2.bark()
