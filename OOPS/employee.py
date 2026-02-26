class Employee:
    def __init__(self,name,ids,salary):
        self.emp_name = name
        self.emp_id = ids
        self.basicSalary = salary
        self.salary = 0
        self.net_salary()

    def calculate_hra(self):
        hra = (self.basicSalary * 20)/100
        return hra

    def calculate_pf(self):
        pf = (self.basicSalary * 12)/100
        return pf

    def net_salary(self):
        s = self.basicSalary
        
        s += self.calculate_hra()
        s -= self.calculate_pf()
        self.salary = s
        

    def breakDown(self):
        print(f"Name: {self.emp_name}")
        print(f"Id: {self.emp_id}")
        print(f"Basic Salary: {self.basicSalary}")
        print(f"HRA: {self.calculate_hra()}")
        print(f"PF: {self.calculate_pf()}")
        print(f"Final Salary: {self.salary}")

name = "Muhsil NR"
ids = 23456789
salary = 57000
e1 = Employee(name,ids,salary)
try:
    while True:
        print("\n\tbreakDown:[1]\tnetSalary:[2]\t Hra:[3]\tQuit[5]")
        x = int(input("Input: "))
        
        if x < 1 or x > 5:
            raise ValueError
        elif x == 5:
            break
        elif x == 1:
            e1.breakDown()
        elif x == 2:
            print(f"\nNet Salary: {e1.salary}\n")
        elif x == 3:
            print(f"\nHra: {e1.calculate_hra()}\n")
        elif x == 4:
            print(f"\nPF; {e1.calculate_pf}\n")
            
except ValueError:
    print("Invalid Value❌")
