class Payment:
    def __init__(self,amount):
        self.amount = amount
        
    def pay(self):
        print("Payment Processing...")
        print(f"amount: {self.amount} sucessful")
        print("Payment method Normal Payment")
class CreditCardPayment:
    def __init__(self,amount):
        self.amount = amount
        
    def pay(self):
        print("Payment Processing...")
        print(f"amount: {self.amount} sucessful")
        print("Payment method Credit Card Payment")

class UPIPayment:
    def __init__(self,amount):
        self.amount = amount
        
    def pay(self):
        print("Payment Processing...")
        print(f"amount: {self.amount} sucessful")
        print("Payment method UPI payment")

class WalletPayment:
    def __init__(self,amount):
        self.amount = amount
        
    def pay(self):
        print("Payment Processing...")
        print(f"amount: {self.amount} sucessful")
        print("Payment method Wallet Payment")

amount = 1000
payment = [
    Payment(1000),
    CreditCardPayment(amount),
    UPIPayment(amount),
    WalletPayment(amount)
]

for type in payment:
    print()
    type.pay()
    print()
        