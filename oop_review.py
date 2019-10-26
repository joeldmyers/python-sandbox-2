# Ye old car class 

class Car:
    # class variables
    runs = True
    number_of_wheels = 4

    #constructor - what to do when instantiating.
    def __init__(self, name):
        print(f"New Car")
        self.name = name
    
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