# 20. Creating a Custom Exception

# Assignment:

# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom Exception: InvalidAgeError
class InvalidAgeError(Exception):
    """Exception raised for invalid age (less than 18)."""
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid!")

# --- Testing the custom exception with try...except ---
try:
    age = int(input("Enter your age: "))  # Get user input
    check_age(age)  # Check if the age is valid
except InvalidAgeError as e:
    print(f"Invalid age: {e.age} - {e.message}")
