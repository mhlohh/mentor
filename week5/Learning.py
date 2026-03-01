from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self,course_name,duration):
        self.course_name = course_name
        self.duration = duration
    @abstractmethod
    def course_details():
        pass
    
class ProgrammingCourse(Course):
    def __init__(self):
        super().__init__("Programming Course",4)
    
    def course_details(self):
        print(f"Course: {self.course_name}")
        print(f"Duration: {self.duration}")
        

class DesignCourse(Course):
    def __init__(self):
        super().__init__("Design Course",3)
    
    def course_details(self):
        print(f"Course: {self.course_name}")
        print(f"Duration: {self.duration}")
        
class MarketingCourse(Course):
    def __init__(self):
        super().__init__("Marketing Course", 3)
    
    def course_details(self):
        print(f"Course: {self.course_name}")
        print(f"Duration: {self.duration}")
        
programms = [
    ProgrammingCourse(),
    DesignCourse(),
    MarketingCourse()
]

for pmg in programms:
    print()
    pmg.course_details()
    print()