#Parent class for Inhertance or base class
class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def printName(self):
        print(self.firstName,self.lastName)

#student class inherited properties of parent class from the Person class
class Student(Person):
    def __init__(self,fname,lname,graduateYear):
        super().__init__(fname,lname)
        self.graduateYear = graduateYear
        
s1 = Student("Mushil","NR",2005)

s1.printName() #printName is Person function no student but it is inherited for the parent class
print(s1.graduateYear) #this sutdent funciton class 

# Create a class
class Person:
   def __init__(self,name,age):
       self.name = name
       self.age = age
   def greet(self):
       print(f"Hello, my name is {self.name}")
# Create an object
p1 = Person("Mushil NR",20)
# Call the greet method
p1.greet()

