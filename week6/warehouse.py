from abc import ABC, abstractmethod
class WarehouseEntity(ABC):
    def __init__(self,name,qty,price):
        self._name = name
        self._qty = qty
        self._price = price
        
    @property
    def name(self):
        return self._name
    
    @property
    def qty(self):
        return self._qty
    
    @property
    def price(self):
        return self._price
    @abstractmethod
    def display_dtails(self):
        pass
        

class Product(WarehouseEntity):
    def __init__(self, name, qty, price):
        super().__init__(name, qty, price)
    
    def display_dtails(self):
        print("----Product----")
        print(f"\nName: {self.name}")
        print(f"QTY: {self.qty}")
        print(f"Price: {self.price}")
        print(f"TotalPrice: {self.price * self.qty}\n")

class Supplier(WarehouseEntity):
    def __init__(self, name, qty, price):
        super().__init__(name, qty, price * 1.2 )
        
    def display_dtails(self):
        print("---Supplier---")
        print(f"\nName: {self.name}")
        print(f"QTY: {self.qty}")
        print(f"Price: {self.price}")
        print(f"TotalPrice: {self.price * self.qty}\n")


p1 = Product("Paste",10,20)
p1.display_dtails()
p2 = Supplier("Paset",10,20)
p2.display_dtails()