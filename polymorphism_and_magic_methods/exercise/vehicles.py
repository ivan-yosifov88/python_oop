from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


def is_fuel_enough(consumption, extra_consumption, fuel_quantity, kilometers, needed_fuel):
    return needed_fuel <= fuel_quantity


def get_needed_fuel(consumption, extra_consumption, kilometers):
    consumption += extra_consumption
    return consumption * kilometers


class Car(Vehicle):
    EXTRA_SUMMER_FUEL_CONSUMPTION = 0.9

    def drive(self, kilometers):
        needed_fuel = get_needed_fuel(self.fuel_consumption, Car.EXTRA_SUMMER_FUEL_CONSUMPTION, kilometers)
        if is_fuel_enough(self.fuel_consumption, Car.EXTRA_SUMMER_FUEL_CONSUMPTION, self.fuel_quantity, kilometers, needed_fuel):
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_SUMMER_FUEL_CONSUMPTION = 1.6

    def drive(self, kilometers):
        needed_fuel = get_needed_fuel(self.fuel_consumption, Truck.EXTRA_SUMMER_FUEL_CONSUMPTION, kilometers)
        if is_fuel_enough(self.fuel_consumption, Truck.EXTRA_SUMMER_FUEL_CONSUMPTION, self.fuel_quantity, kilometers, needed_fuel):
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

