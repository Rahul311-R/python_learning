from abc import ABC, abstractmethod

class Vehicle(ABC):          # abstract class
    @abstractmethod
    def start(self):
        pass                 # no implementation here

class Car(Vehicle):          # subclass
    def start(self):
        print("Car started with key")

class Bike(Vehicle):         # another subclass
    def start(self):
        print("Bike started with button")

c = Car()
c.start()

b = Bike()
b.start()
