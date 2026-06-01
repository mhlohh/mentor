from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self,ticketPrice,seatAvailable):
        self._ticketPrice = ticketPrice
        self.seatAvailable = seatAvailable
        
    @property
    def ticketPrice(self):
        return self._ticketPrice
    
    @property
    def seatAvailable(self):
        return self.seatAvailable
    @abstractmethod
    def book_ticket(self):
        pass
class Bus(Transport):
    def __init__(self,price):
        self.price = price
        
        
    def book_ticket(self,seats):
        super().__init__(self,self.price,seats)
        if seats > self.seatAvailable:
            raise ValueError(f"max available seats{self.seatAvailable}")
        print(f"Bus Ticket Booked☑️ {seats * self.price * seats}")
        
        
    

class Train(Transport):
    def __init__(self,price):
        self.price = price
        
        
    def book_ticket(self,seats):
        super().__init__(self,self.price,seats)
        if seats > self.seatAvailable:
            raise ValueError(f"max available seats{self.seatAvailable}")
        print(f"Train Ticket Booked☑️ {seats * self.price * seats}")
        
        

