# 19. callable() and __call__()

# Assignment:

# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a functio

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # The factor to multiply by

    def __call__(self, value):
        """This method is called when the object is used like a function."""
        return value * self.factor

# --- Testing the Multiplier class with __call__ and callable() ---
multiplier = Multiplier(5)  # Create a Multiplier object with factor 5

# Check if the object is callable
print(callable(multiplier))  # True, because __call__ is defined

# Call the object like a function
result = multiplier(10)  # Equivalent to multiplier.__call__(10)
print(f"10 multiplied by factor 5 is: {result}")
