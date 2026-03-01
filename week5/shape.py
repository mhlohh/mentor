from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def draw():
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def draw():
        print("()")
    
    def area(self):
        return f"{3.14*self.radius**2}cm\u00b2"

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width =width
        self.length = length
    
    def draw():
        print("[]")
    
    def area(self):
        return f"{self.length*self.width}cm\u00b2"

class Triangle(Shape):
    def __init__(self,base,heigth):
        self.base = base
        self.heigth = heigth
    def draw():
        print("/_\\\\")
    def area(self):
        return f"{0.5* self.heigth* self.base}cm\u00b2"

shapes = [
    Circle(radius=4),
    Rectangle(width=30,length=100),
    Triangle(base= 30,heigth=60)
]

for sh in shapes:
    print(sh.area())

