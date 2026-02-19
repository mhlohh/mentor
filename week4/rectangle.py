class Rectangle:
    def __init__(self,length,breadth):
        self.lenght = length
        self.breadth = breadth
    
    def calculate_area(self):
        area = self.lenght * self.breadth
        return area
    
    def update_dimensions(self,new_length, new_breadth):
        self.lenght = new_length
        self.breadth = new_breadth

   

try: 
    length  = int(input('Enter the length: '))
    if length < 1:
        raise ValueError
        
    breadth = int(input("Enter the breadth: "))
    if breadth <1:
        raise ValueError
    r1 = Rectangle(length,breadth)
    while True:
        print("Calculate Area [1]\tupdate dimension [2]\tQuit [3]")
        x = int(input("Input: "))
        if x < 1 or x >3:
            raise ValueError
        elif x == 3:
            break
        elif x == 1:
            area = r1.calculate_area()
            print(f"\nArea : {area}\n")
        elif x == 2:
            l = int(input("\nUpdate length: "))
            print()
            if l < 1:
                raise ValueError
            w = int(input("\nUpdate the width:"))
            print()
            if w <1:
                raise ValueError
            r1.update_dimensions(l,w)
except ValueError:
   print("Invalid Input ❌\n")
    
