import datetime

# Ye old car class 

class Car:
    # class variables
    runs = True
    number_of_wheels = 4

    #constructor - what to do when instantiating.
    def __init__(self, name):
        print(f"New Car")
        self.name = name

    # programmer friendly explanation of this
    def __str__(self):
        return f"This is a human readable description of my car {self.name}"

    def __repr__(self):
        # show all params needed
        return f"Car({self.name})"
    
    def start(self): 

        if self.runs:
            print(f"{self.name} car is started")
        else: 
            print(f"{self.name} car is broken")

    # use this decorator to create a class method
    @classmethod
    def get_number_of_wheels(cls):
        # this is how class methods pass instance
        return cls.number_of_wheels


my_subaru = Car("Subaru")

print(type(my_subaru))

my_subaru.start()

my_subaru.runs = False

my_subaru.start()

print(Car.get_number_of_wheels())

print(isinstance(my_subaru, Car))

# str and repr

# repr is for the system, how to tell the system how it works.

# ex: 

now = datetime.datetime.now()
str(now)
print(repr(now))

print(str(my_subaru))
print(repr(my_subaru))
