class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        pass
class Passenger(Person):
    def __init__(self, name, age,start,destination,cost):
        super().__init__(name, age)
        self._start = start
        self._destination = destination
        self._cost = cost
    @property
    def start(self):
        return self._start
    
    @property
    def destination(self):
        return self._destination
    
    @property
    def cost(self):
        return self._cost
        
        
    
    def display_info(self):
        print("\n------Passenger------")
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Destination: {self.destination}")
        print(f"FROM: {self.start}")
        print(f"Cost: {self.cost}\n")
        
class Staff(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
    def display_info(self):
        print("\n------Staff------")
        print(f"\nCrew Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Destination: {self}")
        print(f"No: {self.roll_no}\n")


person = Passenger(name= "Muhsil NR",age= 19,destination="Sharjah",start="Trivandrum,Kerala",cost=300000)
person.display_info()

staff = Staff(name= "Abhishek",age=30,roll_no=12)
staff.display_info()
        
        
        