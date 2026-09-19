class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        print(f"{self.brand} is a vehicle.")


class Car(Vehicle):
    def describe(self):
        print(f"{self.brand} is a car with four wheels.")


class Bike(Vehicle):
    def describe(self):
        print(f"{self.brand} is a bike with two wheels.")


if __name__ == "__main__":
    vehicles = [Vehicle("Generic"), Car("Toyota"), Bike("Yamaha")]

    for v in vehicles:
        v.describe()
