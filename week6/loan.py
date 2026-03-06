from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self,balacnce):
        self._balance = balacnce
        
    def deposit(self,amount):
        if amount < 1:
            raise ValueError("amount should be positive")
        self._balance += amount
        print(f"{amount} is deposited ☑️") 
        
  
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be posititve ❌")
        if amount > self._balance:
            raise ValueError("Insufficent funds❌")
        self._balance -= amount
        print(f"{amount} is withdrawd ☑️")
        
    @abstractmethod
    def calculate_interest(self):
        pass
    
    @property
    def balance(self):
        return self._balance

class SavingsdAccount(Account):
    def __init__(self, balacnce,interest):
        super().__init__(balacnce)
        self.__interest = interest
    @property
    def interests(self):
        return self.__interest
    def calculate_interest(self):
        amount = self.balance 
        amount = (amount * self.interests)/100
        return amount
    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self, amount):
        return super().withdraw(amount)
    
class CurrentAccount(Account):
    def __init__(self, balacnce):
        super().__init__(balacnce)
    def calculate_interest(self):
        return 0
    def deposit(self, amount):
        return super().deposit(amount)
    def withdraw(self, amount):
        return super().withdraw(amount)
    
class LoanAcoount(Account):
    def __init__(self, balacnce,interest):
        super().__init__(balacnce)
        self.__interest = interest
    @property
    def intrests(self):
        return self.__interest
    def calculate_interest(self):
        amount = self.balance 
        amount = (amount * self.intrests)/100
        return amount
    
    def deposit(self, amount):
        return super().deposit(amount)
    
    

c1 = LoanAcoount(12000,12)
print(c1.balance)
print(c1.calculate_interest())
c2 = CurrentAccount(3000)
print(c2.balance)
print(c2.calculate_interest())
c3 = SavingsdAccount(40000,3.5)
print(c3.calculate_interest())
c3.deposit(30000)
print(c3.balance)
c3.withdraw(1000)
print(c3.balance)