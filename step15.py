# 15. Method Resolution Order (MRO) and Diamond Inheritance

# Assignment:

# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

# Base class A
class A:
    def show(self):
        print("A's show() method")

# Class B inheriting from A
class B(A):
    def show(self):
        print("B's show() method")

# Class C inheriting from A
class C(A):
    def show(self):
        print("C's show() method")

# Class D inheriting from both B and C
class D(B, C):
    pass

# --- Testing MRO ---
d = D()
d.show()  # Which show() method will be called?
