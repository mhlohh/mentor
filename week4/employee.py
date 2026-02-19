class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def increase_salary(self,amount):
        if amount < 0:
            raise ValueError("put valid inputs ❌")
        self.salary += amount
        print(f"{amount} is added to salary succesfully ☑️")
        
    def display_details(self):
        print()
        print(f"{self.name}")
        print(f"{self.id}")
        print(f"{self.salary}\n")

name = "Mushil NR"
ID = 1234888
salary = 2500000
e1 = Employee(name,ID,salary)  
try:
    while True:
        print("Employee Details[1]\tIncrease Salary[2]\tQuit[3]")
        x = int(input("Input: "))
        if x < 1 or x > 3:
            raise ValueError
        elif x == 3:
            break
        elif x == 1:
            e1.display_details()
        elif x == 2:
            print()
            amount = int(input("Salary Increase: "))
            print()
            if amount < 1:
                raise ValueError
            e1.increase_salary(amount)

except ValueError:
    print("Invalid Input ❌\n")