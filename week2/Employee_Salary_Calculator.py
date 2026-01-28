class employees:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    
    def gross_salary(self,salary,other_expenses):
        returnGrossSalary = salary + other_expenses
        return returnGrossSalary
    
    def deduction(self,value,other_expenses):
        self.gross_salary(value,other_expenses)