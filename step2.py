# 2. Using cls

# Assignment:

# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # Class variable to keep track of the number of objects

    def __init__(self):
        Counter.count += 1  # Increment count whenever a new object is created

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")  # Display the count using the class variable

# Example usage:
obj1 = Counter()  # Create first object
obj2 = Counter()  # Create second object
obj3 = Counter()  # Create third object

# Display the number of objects created
Counter.display_count()  # This will show 3, since 3 objects have been created
