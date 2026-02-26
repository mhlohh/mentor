class BankAccount:

    def __init__(self,name,acNum):

        self.account_holder = name
        self.account_number = acNum
        self.balance = 0.0
    

    def deposit(self,amount):
        if amount < 0:
            raise ValueError("\namount should be positive❌\n")
        self.balance += amount
        print(f"\n{amount} deposited Sucessfully☑️\n")

    def withdraw(self,amount):
        if amount < 0 or amount > self.balance:
            raise("\nInsufficent Fund❌\n")
        self.balance -= amount
        print(f"\n{amount} is withdraw Sucessfully☑️\n")

    def checkBalance(self):
        return self.balance

name = "Muhsil NR"
acNum = 123556

person = BankAccount(name,acNum)

while True:
    try:
        print("Deposit[1]\twithdraw[2]\tcheckBalance[3]\tQuit[4]")
        x = int(input("Input: "))
        if x < 1 or x > 4:
            raise ValueError("\nInput out of bound❌\n")
        if x == 4:
            break
        
        elif x == 1:
            amount = int(input("amount: "))
            person.deposit(amount)
            
        elif x == 2:
            amount = float(input("amount: "))
            person.withdraw(amount)
            
        elif x == 3:
            print(f"\nBalance: {person.checkBalance()}\n")
            
    except ValueError:
        print("\nInvalid Input❌\n")
            
                           
            
        
