class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model} car with {self.fuel} as fuel"

class Car(Vehicle):
    number_of_wheels = 4

    # no constructor, so it uses the parent class's constructor.

class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

my_car = Vehicle("Toyota", "Camry")

print(f"My car runs on {my_car.fuel}")
print(my_car)
my_truck = Truck("Ford", "F150")

print(my_truck.number_of_wheels)