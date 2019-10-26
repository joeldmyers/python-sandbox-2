# Ye old car class 
# (haha)

class Car:
    runs = True
    
    def start(self, name): 
        # self is associated with the instance.  
        self.name = name

        if self.runs:
            print(f"{self.name} car is started")
        else: 
            print(f"{self.name} car is broken")


my_subaru = Car()

print(type(my_subaru))

my_subaru.start("Subaru")

my_subaru.runs = False

my_subaru.start("Subaru")