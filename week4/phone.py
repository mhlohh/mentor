class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def apply_discount(self,discount_amount):
        if discount_amount > self.price or discount_amount < 1:
            raise ValueError
        price = self.price
        price -= discount_amount
        return price
    
    def display_mobile(self):
        print()
        print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}\n")

brand = "Motorola"
model = "g31"
PRICE = 12000
m1 = Mobile(brand,model,PRICE)
try:
    while True:
        print("Discount[1]\tDisplay Mobile[2]\tQuit[3]")
        x = int(input("Input: "))
        if x < 1 or x > 3:
            raise ValueError
        elif x == 3:
            break
        elif x ==1 :
            print()
            amount = int(input("Amount: "))
            discountedPrice = m1.apply_discount(amount)
            print(f"Discounted Prce: {discountedPrice}\n")
        elif x == 2:
            m1.display_mobile()
except ValueError:
    print("Invalid Input ❌\n")