movie_seat = {"The God Father":0,"The Dark Knight":0,"The inception":0}
def max_moive(name,seat):
    if movie_seat[name] <= 50:
        movie_seat[name]+= seat
    else:
        raise ValueError("Seats Filled")
    
class person:
    def __init__(self,name,movie_no,seats):
        
        self.name = name
        self.seat = seats
        self.movie_no = movie_no
        self.movie_name = ['The God Father','The Dark Knight','The inception']
        self.movie =  self.movie_name[self.movie_no]
        self.booking()
        
    
    def booking(self):
        
        self.movie = self.movie_name[self.movie_no]
        max_moive(self.movie,self.seat)
        
    def printRecipt(self):
        print(f"Name: {self.name}")
        print(f"{self.movie}")
        print(f"{self.seat}")
        
try:
    print("\tBook Ticket[1]\t")
    x = int(input("Input: "))
    if x == 1:
        name = input("Enter the name: ")
        print("\nThe God Father[1]\tThe Dark Knight[2]\tThe inception[3]\n")
        movie_name = int(input("Enter the moive name: "))
        if movie_name < 1 or movie_name >3:
            raise ValueError("Value out of bound❌")
        seat = int(input("Enter the seats: "))
        if seat < 1:
            raise ValueError("Invalid Input")
        if seat > 50:
            raise ValueError("Max Value is 50")
        p = person(name,(movie_name - 1),seat)
        print()
        p.printRecipt()
    else:
        raise ValueError("Value out of bound❌")
        
        
    
except ValueError as e:
    print("Invalid Input❌")
    

        


