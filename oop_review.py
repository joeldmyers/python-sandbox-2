# Ye old car class 
# (haha)

class Car:
    run = True
    
    def start(self, name): 
        # self is associated with the instance.  
        self.name = name

        if self.runs:
            print(f"{self.name} car is started")
        else: 
            print(f"{self.name} car is broken")