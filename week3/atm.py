import sys


class atm:
    def __init__(self):
        self.balance = 10000
        self.password = "9887"

    def withdrawl(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def account_balance(self):
        return self.balance

    def checkPassword(self, key):
        if self.password == key:
            return True
        else:
            return False


client = atm()
amount = 0
while True:
        try:
            password = input("password: ")
            if client.checkPassword(password) == False:
                raise ValueError()
            x = int(
                input(f"\tCash Withdrawls[1]\tCash Deposit[2]\t\tAccount Balance[3]\tQuit[4]\n\nInput: "))
            print()


            if (x < 1 or x > 4):
                raise ValueError()
            if x == 4:
                print("Thankyou !\n")
                break
            elif x != 3:
                amount = int(input("Enter the amount: "))
                print()
            if amount < 0:
                raise ValueError()
            elif x == 1:
                if client.account_balance() < amount:
                   print("Insufficent Fund")
                   continue
                client.withdrawl(amount)
                print(f"amount: {amount} withdrwn Succesfully! ☑️\n")
            elif x == 2:
                client.deposit(amount)
                print(f"amount {amount} deposited succesfully! ☑️\n")
            elif x == 3:
                print(f"Balance: {client.account_balance()}$\n")

        except ValueError as e:
            print()
            print("Invalid Input !❌")
            print()


