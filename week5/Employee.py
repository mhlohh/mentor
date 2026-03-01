from abc import ABC, abstractmethod
class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
    @abstractmethod
    def calculate_salary(self):
        pass
        
class Manager(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
        
    def calculate_salary(self):
        return self.base_salary * 5
    
    
    
class Developer(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
    def calculate_salary(self):
        return self.base_salary * 3
    
class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
        
    def calculate_salary(self):
        return self.base_salary


employers = [
    Manager("Muhsil NR",100000),
    Developer("PrithNandan",15000),
    Intern("Vijin",10000)
]

for emp in employers:
    print(f"\nName: {emp.name}")
    print(f"Salary: {emp.calculate_salary()}")
    