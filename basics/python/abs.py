from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # Abstract method, no implementation

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key...")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a button...")

car = Car()
bike = Bike()
car.start()  # Output: Car is starting with a key...
bike.start()  # Output: Bike is starting with a button...