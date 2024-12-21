class Vehicle():
    
    def __init__(self,max_speed,milage):
        self.max_speed = max_speed
        self.milage = milage

car = Vehicle(200,15000)
print(f"instance is : {car}")
print(f"attribute is : max_speed = {car.max_speed}, milage = {car.milage}")     