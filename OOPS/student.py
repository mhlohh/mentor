class Student:

    def __init__(self,name,no,python,dsa):
        self.name = name
        self.roll_no = no
        self.marks_python = python
        self.marks_dsa = dsa

    def calculate_average(self):
        avg = (self.marks_python  + self.marks_dsa )/2.0
        return avg

    def display_details(self):
        print(f"\nName: {self.name}")
        print(f"rollNO: {self.roll_no}")
        print(f"Python Mark: {self.marks_python}")
        print(f"Dsa Mark: {self.marks_dsa}")
        print(f"Average Mark: {self.calculate_average()}\n")
    def is_eligible_for_internship(self):
        if self.calculate_average() >= 70:
            return True
        else:
            return False


name = "Muhsil NR"
rollno = 12
pythonMark = 80
dsaMark = 78
student1 = Student(name,rollno,pythonMark,dsaMark)
while True:
    try:
        print("Display Dtails[1]\tAverage[2]\tIs Intership Eligibility[3]\tQuit[4]")
        x = int(input("Input: "))
        if x < 1 or x > 4:
            raise ValueError("\nValue out of bounds❌\n")
        elif x == 4:
            break
        elif x == 1:
            student1.display_details()

        elif x == 2:
            print(f"\nAverage: {student1.calculate_average()}\n")

        elif x == 3:
            print(f"\nEligibility: {student1.is_eligible_for_internship()}\n")
    except ValueError:
       print("\nInvalid Output❌\n")
