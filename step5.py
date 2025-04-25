# 5. Static Variables and Static Methods

# Assignment:

# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# --- Testing the static method ---
print(MathUtils.add(5, 7))     # Output: 12
print(MathUtils.add(-2, 10))   # Output: 8
