# Ye old car class 

class Car:
    runs = True

    def __init__(self, name):
        print(f"New Car")
        self.name = name
    
    def start(self): 

        if self.runs:
            print(f"{self.name} car is started")
        else: 
            print(f"{self.name} car is broken")


my_subaru = Car("Subaru")

print(type(my_subaru))

my_subaru.start()

my_subaru.runs = False

my_subaru.start()