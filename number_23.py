class Vehicle():
    
    def __init__(self,max_speed,milage):
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    
    def __init__(self, max_speed, milage):
        super().__init__(max_speed, milage)
        
      
        
        
tata =  Bus(100,1500)
print(tata.milage)
print(tata.max_speed)   