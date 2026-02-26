class Shopping:
    def __init__(self,name,price,qty):
        self.prod = name
        self.price = price
        self.qty = qty

    def totalPrice(self):
        return self.price * self.qty

    def display(self):
        print(f"\nProduct: {self.prod}")
        print(f"price: {self.price}")
        print(f"QTY: {self.qty}")
        print(f"Total Price: {self.totalPrice()}\n")

    
prod = "Flour"
price = 60
qty  = 5
bill = Shopping(prod,price,qty)

while True:
    try:
        print("Bill[1]\tTotal\tPrice[2]\tQuit[3]")
        x = int(input("Input: "))
        if x < 1 or x > 3:
            print("\nValue out of bound❌\n")
            break
        elif x == 3:
            break
        elif x == 1:
            bill.display()
        elif x == 2:
            print(f"\nTotal Price: {bill.totalPrice()}\n")
    except ValueError:
        print("\nInvalid Input❌\n")
