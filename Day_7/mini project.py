from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    def __init__(self, brand, model):
        self._brand = brand        # encapsulated attribute
        self._model = model

    @abstractmethod
    def start(self):
        pass

    def info(self):
        return f"Brand: {self._brand}, Model: {self._model}"

# Child class 1
class Car(Vehicle):
    wheels = 4    # class variable

    def start(self):                # overriding abstract method
        return f"{self._brand} {self._model} starts with a key"

    def feature(self):
        return "Has air conditioning and airbags"


# Child class 2
class Bike(Vehicle):
    wheels = 2

    def start(self):                # overriding abstract method
        return f"{self._brand} {self._model} starts with a self button"

    def feature(self):
        return "Has disc brakes and good mileage"


# Polymorphism in action
vehicles = [Car("Toyota", "Innova"), Bike("Yamaha", "R15")]

for v in vehicles:
    print(v.info())
    print(v.start())
    print(v.feature())
    print("Wheels:", v.wheels)
    print()
