# Traditional-OOP-Practice

In these project we ha 21 steps to covered OOPS method

# 1. Using self 🧍‍♂️
Task: Create a Student class with attributes name and marks. Initialize them using self in the constructor, and make a display() method to print details.
Goal: Understand how to set up instance variables using self.

# 2. Using cls 🏫
Task: Create a Counter class that tracks how many objects were created. Use a class variable and a class method with cls.
Goal: Learn how to use cls to work with class-level data.

# 3. Public Variables & Methods 🚗
Task: Create a Car class with a public variable brand and a public method start(). Create an object and access both.
Goal: Understand how public variables and methods are accessed from outside the class.

# 4. Class Variables & Methods 🏦
Task: Create a Bank class with a class variable bank_name. Add a class method to change it.
Goal: Show that changing the class variable affects all instances of the class.

# 5. Static Methods ➕
Task: Create a MathUtils class with a static method add(a, b) that returns the sum.
Goal: Learn how to use static methods that don't rely on class or instance data.

# 6. Constructors & Destructors 🔄
Task: Create a Logger class that prints a message when an object is created (constructor) and another when it is destroyed (destructor).
Goal: Understand the use of __init__() and __del__().

# 7. Access Modifiers 🔐
Task: Create an Employee class with:

Public: name

Protected: _salary

Private: __ssn
Try to access them and observe the behavior.
Goal: Learn the difference between public, protected, and private variables.

# 8. The super() Function 👨‍🏫
Task: Create a base class Person and a derived class Teacher that adds subject. Use super() to call the base class constructor.
Goal: Understand inheritance and how super() helps reuse parent class code.

# 9. Abstract Classes and Methods 🧩
Task: Use the abc module to make an abstract class Shape with an abstract method area(). Inherit Rectangle and implement area().
Goal: Learn about abstraction and how to enforce method implementation in subclasses.

# 10. Instance Methods 🐶
Task: Create a Dog class with name, breed, and a method bark() that includes the dog's name in the message.
Goal: Understand instance methods that act on object-specific data.

# 11. Class Methods 📚
Task: Create a Book class with a class variable total_books. Use a class method to increment it whenever a book is added.
Goal: Learn how to modify class variables using class methods.

# 12. Static Methods 🌡️
Task: Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c).
Goal: Use static methods to perform actions without needing an instance.

# 13. Composition 🔧🚗
Task: Create Engine and Car classes. Pass an Engine object to the Car class and use it from there.
Goal: Understand composition – a "has-a" relationship between objects.

# 14. Aggregation 🏢👨‍💼
Task: Create Department and Employee classes. Let Department hold a reference to an Employee object that exists independently.
Goal: Learn aggregation – a weaker form of composition.

# 15. MRO & Diamond Inheritance 💎
Task: Create:

Class A with show()

Classes B and C that inherit from A and override show()

Class D that inherits from both B and C
Create a D object and call show() to see how Method Resolution Order works.
Goal: Understand how Python resolves method calls in multiple inheritance.

# 16. Function Decorators 🎯
Task: Create a decorator log_function_call that prints a message before running a function. Apply it to say_hello().
Goal: Learn how to use function decorators to wrap functions.

# 17. Class Decorators 👋
Task: Create a class decorator add_greeting that adds a greet() method to any class it decorates.
Goal: Use decorators to modify class behavior dynamically.

# 18. Property Decorators 🏷️
Task: Create a class Product with a private _price. Use:

@property to get the price,

@price.setter to set it,

@price.deleter to delete it.
Goal: Learn property decorators for encapsulated access.

# 19. callable() and __call__() ☎️
Task: Create a Multiplier class with a __call__() method that multiplies a number by a factor. Use callable() and call the object like a function.
Goal: Make objects behave like functions using __call__.

# 20. Custom Exception 🚫
Task: Create a custom exception InvalidAgeError. In a function, raise it if age < 18. Handle it with try...except.
Goal: Understand how to define and use custom exceptions.

# 21. Iterable Class 🔁
Task: Create a Countdown class that takes a starting number and implements __iter__() and __next__() to make it work in a for loop.
Goal: Learn how to make your class iterable using the iterator protocol.

# Motivation quote 💻✨

"One bug closer to brilliance." 🐞➡️💡

