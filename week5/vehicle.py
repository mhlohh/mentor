class Vehicle:
    def __init__(self,brand,speed,fuel_type):
        self.brand = brand
        self.speed = speed
        self.fuel_type = fuel_type
        
    def display_inf(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")
        print(f"Fuel_type: {self.fuel_type}")
    
class Car(Vehicle):
    def __init__(self,brand,speed,fuel_type,no_doors):
        self.no_doors = no_doors
        super().__init__(brand,speed,fuel_type)
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")
        print(f"Fuel_type: {self.fuel_type}")
        print(f"No Doors: {self.no_doors}")
    
        
        
class Bike(Vehicle): 
    def __init__(self, brand, speed, fuel_type,engine_capacity):
        super().__init__(brand, speed, fuel_type)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")
        print(f"Fuel_type: {self.fuel_type}")
        print(f"No Doors: {self.engine_capacity}")
        



car = Car("Ford",180,"petrol",4)
bike = Bike("R15",100,"petrol",200)

print()
car.display_info()
print()
bike.display_info()
print()
        
    