
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
        self.paymet_method = "Normal Payment"
        super().__init__(amount,self.paymet_method)
        
class CreditCardPayment(Payment):
    
    def __init__(self,amount):
        self.payment_method = "Credit Card Payment"
        super().__init__(amount,self.payment_method)

    
class UPIPayment(Payment):
    def __init__(self,amount):
        self.payment_method = "UPI Payment"
        super().__init__(amount,self.payment_method)
        
    
class WalletPayment(Payment):
    def __init__(self,amount):
        self.payment_method = "Wallet Payment"
        super().__init__(amount,self.payment_method)
        
    


try:
    amount = int(input("\nEnter Amount: "))
    print("\n\tNormal Payment [1]\tUPI Payment [2]\tCredit Payment [3]\tWallet Payemt [4]\n")
    
    x = int(input("Enter the Input: "))
    print()
    if x < 1 or x > 4:
        raise ValueError("Invalid Input❌")
    elif x == 1:
        pmt = NormalMethod(amount)
        pmt.pay()
    elif x == 2:
        pmt = UPIPayment(amount)
        pmt.pay()
    elif x == 3:
        pmt = CreditCardPayment(amount)
        pmt.pay()
    elif x == 4:
        pmt = WalletPayment(amount)
        pmt.pay()
except ValueError as e:
    print(f"Value Erro: {e}")