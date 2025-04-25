# 16. Function Decorators

# Assignment:

# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()

# Decorator function
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator to a function
@log_function_call
def say_hello():
    print("Hello, world!")

# --- Testing the decorator ---
say_hello()
