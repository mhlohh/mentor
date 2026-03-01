"""What we are doing is we are overriding the pay method with each 
Sub Class Therefore creating a polymorphism"""
class Payment:
    def __init__(self,amount):
        self.amount = amount
        
    def pay(self):
        print("Payment Processing...")
        print(f"Payment Method: Normal {self.amount}")
        
class CreditCardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    
    def pay(self):
        print("Payment Processing...")
        print(f"Payment Method: Normal {self.amount}")

class UPIPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    
    def pay(self):
        print("Payment Processing...")
        print(f"Payment Method: UPI {self.amount}")
        
class WalletPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    
    def pay(self):
        print("Payment Processing...")
        print(f"Payment Method: Wallet {self.amount}")
        

payments = [
    Payment(1000),
    CreditCardPayment(300),
    UPIPayment(4000),
    WalletPayment(3000)
]

for pmt in payments:
    print()
    pmt.pay()
    print()