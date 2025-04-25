# 13. Composition

# Assignment:

# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# Engine class
class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        return f"🔧 {self.type} engine started!"

# Car class with composition
class Car:
    def __init__(self, make, model, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return f"{self.make} {self.model} is starting... {self.engine.start()}"  # Accessing Engine's method

# --- Testing Composition ---
engine = Engine("V8")
car = Car("Ford", "Mustang", engine)

print(car.start_car())
