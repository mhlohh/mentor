class BankAccount:
    def __init__(self,name,acNumber,balance):
        self.name = name
        self.acNumber = acNumber
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print()
        print(f"{amount} is deposited ☑️\n")
        
    def withdrawl(self,amount):
        if amount > self.balance:
            raise print("Insufficent Fund")
        self.balance -= amount
        print(f"{amount} is withdrawl sucessfully ☑️\n")
    
    def display(self):
        print()
        print(f"Name: {self.name}")
        print(f"Account Number: {self.acNumber}")
        print(f"Balance: {self.balance}\n")
       

name = "Muhsil NR"
balance = 12000
number = 23456789
costumer = BankAccount(name,number,balance)
try:
    while True:
        print("Deposit Money[1]\tWithdraw Money[2]\tCheck balance[3]\tQuit[4]")        
        x = int(input("Input: "))
        if x < 1 or x > 4:
            raise print("Input out of bound❌")
        if x == 4:
            break
        elif x == 1:
            print()
            amount = int(input("Enter the deposit amount: "))
            costumer.deposit(amount)
        elif x == 2:
            print()
            amount = int(input("Enter the withdrawl amount: "))
            print()
            costumer.withdrawl(amount)
        elif x == 3:
            costumer.display()
        
            
except ValueError as e:
    raise ValueError