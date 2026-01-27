import sys
class students:
    def __init__(self,name,attendance):
        self.name = name
        self.attendance= attendance
    fee = 0

students_list = []

fees_dict = {"Full fee" : 0,
                 "Quarter fee" : 0,
                 "Half fee": 0}

numberStudents = int(input("Enter the number of Students(Max 10): "))

if numberStudents > 10 and numberStudents < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberStudents):

    name = input("Enter the name: ")
    attendance = int(input("Enter the Attendance in percentage: "))

    if attendance > 100 and attendance < 0:
        print("Invalid attendance")
        sys.exit()

    student = students(name,attendance)

    print()

    if student.attendance >= 90 :

        print("Full Fee")
        student.fee = 'Full Fee'
        fees_dict["Full fee"] += 1
        

    elif student.attendance >= 75 and student.attendance <= 89:
        
        print("Quarter of Fees")
        student.fee = 'Quarter of Fees'
        fees_dict["Quarter fee"] += 1

    elif student.attendance < 75:

        print("Half of the Fee")
        student.fee = 'Half Fee'
        fees_dict["Half fee"] += 1

    print()
    students_list.append(student)


for std in students_list:
    print(f"Name: {std.name}")
    print(f"speed: {std.attendance}")
    print(f"Fine: {std.fee}")
    print()

print(fees_dict)