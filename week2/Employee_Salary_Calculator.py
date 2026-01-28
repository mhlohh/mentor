class employees:
    def __init__(self,name,id,age,hour,salary):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary
        self.hour = hour
        self.hourlyRate = 500
        self.tax = 15
    def gross_salary(self):
        other_expenses = (self.hour * self.hourlyRate)
        returnGrossSalary = self.salary + other_expenses
        return returnGrossSalary
    
    def deduction(self):
        grossSalary = self.gross_salary()
        returnDeduction = grossSalary - (grossSalary * (self.tax/100)) 
        return returnDeduction

    def final_salary(self):

        finalSalary = self.gross_salary() + (self.deduction)

        return finalSalary
    def employee_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"Gross Salary: {self.gross_salary()}")
        print(f"Deduction: {self.deduction()}")
        print(f"final Salary: {self.final_salary}")
    
name = input("Enter the name: ")
id = int(input("Emplyer id number: "))
age = int(input("Enter the emplyee age: "))
hours = int(input("Enter the working hours: "))
salary = int(input("Enter the your salary: "))
employe = employees(name,id,age,hours,salary)

employe.employee_profile()