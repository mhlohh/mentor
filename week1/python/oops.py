#example class and object
class Computer:
    #object
    #method
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        
        print("This is i5 , 16gb, 1Tb")

    #variables 
    name = "Muhsil NR"
    age = 20

com1 = Computer('i5',16)
com2 = Computer('ryzen 5',8)
print(type(com1))
print(com1.age)
print(com1.name)
com1.config()
print(com1.ram)
print(com2.ram)
print(com1.cpu)
print(com2.cpu)