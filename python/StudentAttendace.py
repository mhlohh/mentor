import sys
class person:
    def __init__(self,name,attendance):
        self.name = name
        self.attendance = attendance

    examEligiblity = ''

students_list = []

student_dict = {"Eligible for exam" : 0,
                 "Conditionally eligible" : 0,
                 "Not eligible": 0
            }

numberStudent = int(input("Enter the number of Employee(Max 10): "))

if numberStudent > 10 and numberStudent < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberStudent):

    name = input("Enter the name: ")
    attendance = int(input("Enter the attendance: "))

    student = person(name,attendance)

    print()

    if student.attendance >= 85:

        student.examEligiblity = 'Eligible for exam'
        print(student.examEligiblity)
        student_dict[student.examEligiblity] += 1
        

    elif student.attendance >= 75 and student.attendance <= 84:

        student.examEligiblity = 'Conditionally eligible'
        print(student.examEligiblity)
        student_dict[student.examEligiblity] += 1
        

    elif student.attendance < 75:

        student.examEligiblity = 'Not eligible'
        print(student.examEligiblity)
        student_dict[student.examEligiblity] += 1

    print()
    students_list.append(student)

for std in students_list:
    print(f"Name: {std.name}")
    print(f"Hours: {std.attendance}")
    print(f"Overtime Pay: {std.examEligiblity}")
    print()

print(student_dict)