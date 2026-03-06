from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @abstractmethod
    def display_role(self):
        pass
        
class Student(Person):
    def __init__(self, name, age,roll_no,mark):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.mark = mark
    def display_role(self):
        return "Student"
    def calculate_grade(self):
        if self.mark > 90:
            return "A"
        elif self.mark >85:
            return "B"
        elif self.mark > 75:
            return "C"
        elif self.mark > 65:
            return "D"
        else:
            return "F"
        
class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject
    def display_role(self):
        return "Teacher"
        
SchoolList = [
    Student("Muhsil NR",21,12,70),
    Student("Abhishek",18,32,90),
    Student("Prithunandan",19,30,100),
    Student("Afluu",19,10,78),
    Teacher("Reshma",40,"Addon"),
    Teacher("Athulya",29,"Graphics")
]

    

for std in SchoolList:
    print(f"Role: {std.display_role()}")
