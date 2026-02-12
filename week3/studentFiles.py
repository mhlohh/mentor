class students:
    def __init__(self):
        self.name
        self.mark

    def average(self):
        pass

    def add_students(self,name,marks):
        try:
            if marks < 1 or marks > 100:
                raise ValueError
            self.name = name
            self.marks = marks
        except ValueError:
            print("Error")
    
    def readStudent(self):
        print()
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}\n")

    
        
        
        



studentList = []


