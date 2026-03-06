from abc import ABC, abstractmethod
class User:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    
    @abstractmethod
    def calculate_fare(self):
        pass
class Driver(User):
    def __init__(self, name, age):
        super().__init__(name, age)
    def calculate_fare(self):
        print("No fare for Driver")

class Passanger(User):
    def __init__(self, name, age,distance):
        super().__init__(name, age)
        self.distance = distance
    def calculate_fare(self,rate_km):
        return rate_km * self.distance
    
pas = Passanger("Muhsil NR",19,20)
print("--------Passanger Detials-------")
print(f"Passanger Name: {pas.name}")
print(f"Age: {pas.age}")
print(f"Fare: {pas.calculate_fare(rate_km=2)}\n")

driver = Driver("Pogacar",29)
print("--------Driver Detials-------")
print(f"Driver Name: {driver.name}")
print(f"Age: {driver.age}")
print(f"{driver.calculate_fare()}")


        
        
    

    