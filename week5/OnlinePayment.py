class Payment:

    def pay(self,amount):
        print(f"Normal Method: {amount}")

class CreditCardPayment:
    
    def pay(self,amount):
        print(f"Normal Method: {amount}")
        
class UPIPayment:
    
    def pay(self,amount):
        print(f"UPI Method: {amount}")
        
class WalletPayment:
    
    def pay(self,amount):
        print(f"Wallet Method: {amount}")

amount = 1000    
pay = [Payment(),CreditCardPayment(),UPIPayment(),WalletPayment()]

for pmt in pay:
    print()
    pmt.pay(amount)
    print()