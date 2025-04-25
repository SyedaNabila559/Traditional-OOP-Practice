# 6. Constructors and Destructors

# Assignment:

# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("📥 Logger object created.")

    def __del__(self):
        print("🗑️ Logger object destroyed.")

# --- Creating and destroying an object ---
def run_logger():
    log = Logger()
    print("📝 Doing some logging...")

run_logger()

# Outside the function, 'log' goes out of scope and gets destroyed
