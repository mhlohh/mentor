import sys
class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    status = ''

status_dict = {"Distinction": 0,
               "Pass" : 0,
               "Fail" : 0}

student_list = []

numberStudents = int(input("Enter the number of Students(Max 10): "))

if numberStudents > 10:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberStudents):

    name = input("Enter the name: ")
    mark = int(input("Enter the mark: "))
    student = students(name,mark)

    print()

    if student.marks >= 75:

        student.status = "Distinction"
        print(f"Status: {student.status} 👨‍🎓")
        status_dict["Distinction"] += 1

    elif student.marks >= 50 and student.marks <= 74:
        
        student.status = "Pass"
        print(f"Status: {student.status} ✅")
        status_dict["Pass"] += 1

    elif student.marks < 50:

        student.status = "Fail"
        print(f"Status: {student.status} ❌")
        status_dict["Fail"] += 1

    print()
    student_list.append(student)

for std in student_list:
    print(f"Name: {std.name}")
    print(f"Mark: {std.marks}")
    print(f"Status: {std.status}")
    print()

print(status_dict)