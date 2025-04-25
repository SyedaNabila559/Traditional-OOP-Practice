# 7. Access Modifiers: Public, Private, and Protected

# Assignment:

# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected (by convention)
        self.__ssn = ssn          # Private (name mangling)

# Create an object
emp = Employee("Alice", 50000, "123-45-6789")

# Accessing variables
print("Public: ", emp.name)        # ✅ Accessible

print("Protected: ", emp._salary)  # ⚠️ Accessible, but by convention should be protected

# Accessing private variable (will raise AttributeError if accessed directly)
try:
    print("Private: ", emp.__ssn)  # ❌ Not directly accessible
except AttributeError as e:
    print("Private: ❌ Cannot access directly ->", e)

# Accessing private variable using name mangling (not recommended, but possible)
print("Private (via mangling): ", emp._Employee__ssn)  # ✅ Accessible, but breaks encapsulation
