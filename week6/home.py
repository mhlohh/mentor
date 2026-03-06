from abc import ABC, abstractmethod
class Devices:
    def __init__(self,status):
        self.status = status
    @abstractmethod
    def operate(self):
        pass
    

class Light(Devices):
    def __init__(self):
        pass
    def operate(self):
        status = "The ligth is on"
        self.status = status
        return status
    
        

class Fan(Devices):
    def __init__(self):
        pass
    def operate(self):
        status = "Fan is running"
        self.status = status
        return "Fan is ON"

class AirConditioner(Devices):
    def __init__(self):
        pass
    def operate(self):
        status = "AC is ON"
        self.status = status
        return status


d1 = Light()
print(f"Operate: {d1.operate()}")
d2 = Fan()
print(f"Operate: {d2.operate()}")
d3 = AirConditioner()
print(f"Operate: {d3.operate()}")
