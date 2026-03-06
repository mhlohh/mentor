class Vehicle:
    def __init__(self,name,licenceNo,time):
        self.name = name
        self.licenceNo = licenceNo
        self._time = time
    
    @property
    def time(self):
        return self._time
    
    
        

class Car(Vehicle):
    def __init__(self, name, licenceNo, timeIN, timeOut):
        super().__init__(name, licenceNo, timeIN, timeOut)
        self.fare = 30
    
    def calculate_fee(self):
        cost = self.fare * self.time
        return cost

class Bike(Vehicle):
    def __init__(self, name, licenceNo, time):
        super().__init__(name, licenceNo, time)
        self.fare = 10
    
    def calculate_fee(self):
        cost = self.fare * self.time
        return cost

class Truck(Vehicle):
    def __init__(self, name, licenceNo, time):
        super().__init__(name, licenceNo, time)
        self.fare = 50
    
    def calculate_fee(self):
        cost = self.fare * self.time
        return cost
    
v1 = Bike("Pulsar",12345678,5)
print(f"Fare: {v1.calculate_fee()}")