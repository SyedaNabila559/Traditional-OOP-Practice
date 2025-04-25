# 18. Property Decorators: @property, @setter, and @deleter

# Assignment:

# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter method for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter method for price with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter method for price"""
        print("Deleting price...")
        del self._price

# --- Testing the Product class with property decorators ---
product = Product(100)

# Getting the price
print(f"Initial price: ${product.price}")

# Setting the price
product.price = 150
print(f"Updated price: ${product.price}")

# Trying to set a negative price (should raise an error)
try:
    product.price = -50
except ValueError as e:
    print(f"Error: {e}")

# Deleting the price
del product.price
