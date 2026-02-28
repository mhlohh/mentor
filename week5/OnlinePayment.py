
class Payment:
    def __init__(self,amount,method):
        self.amount = amount
        self.paymet_method = method
        
    def pay(self):
        print("Payment Processing...")
        print(f"amount: {self.amount} sucessful")
        print(f"Payment Method: {self.paymet_method}\n")

class NormalMethod(Payment):
    
    def __init__(self,amount):
        
        super().__init__(amount,"Normal Payment")
        
class CreditCardPayment(Payment):
    
    def __init__(self,amount):
        super().__init__(amount,"Credit Card Payment")

    
class UPIPayment(Payment):
    def __init__(self,amount):
        
        super().__init__(amount,"UPI Payment")
        
    
class WalletPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount,"Wallet Payment")
        

try:
    amount = int(input("\nEnter Amount: "))
    print("\n\tNormal Payment [1]\tUPI Payment [2]\tCredit Payment [3]\tWallet Payemt [4]\n")
    
    x = int(input("Enter the Input: "))
    print()
    pmt = None
    if x < 1 or x > 4:
        raise ValueError("Invalid Input❌")
    elif x == 1:
        pmt = NormalMethod(amount)
    elif x == 2:
        pmt = UPIPayment(amount)
        
    elif x == 3:
        pmt = CreditCardPayment(amount)
    elif x == 4:
        pmt = WalletPayment(amount)
    if pmt:
        pmt.pay()

except ValueError as e:
    print(f"Value Erro: {e}")