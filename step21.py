# 21. Make a Custom Class Iterable

# Assignment:

# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start  # Starting number for countdown
        self.current = start  # Current number to be used for iteration

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Return the next value in the countdown"""
        if self.current <= 0:
            raise StopIteration  # Stop iteration when countdown reaches 0
        self.current -= 1  # Decrement the countdown
        return self.current + 1  # Return the current value before decrementing

# --- Testing the Countdown class ---
countdown = Countdown(5)  # Countdown starts from 5

# Using the Countdown object in a for-loop
for num in countdown:
    print(num)
