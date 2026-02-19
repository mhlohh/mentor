# Create a class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello my name is {self.name}")

p1 = Person("Muhsil NR",20)
p1.greet()
print(p1.age)
