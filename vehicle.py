

# First note, issubclass(class, possibleParentClass)

# In python, you can inherit from multiple classes. 
# This allows mixins that give certain methods.  for ex., for DB handling dates to get extra date methods.

class Vehicle: 

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel
    
    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True

# subclass
class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", num_wheels=4):
        super().__init__(make, model, fuel)
        self.num_wheels = num_wheels
    

first_car = Vehicle("Toyota", "Prius", "electricity")

print(first_car.model)

my_second_car = Car("Subaru", "Cross Trek", "diesel")

print(f"My car has {my_second_car.num_wheels} wheels")