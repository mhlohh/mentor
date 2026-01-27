
class students:
    def __init__(self,name,mark):
        self.name = name
        self.marks = mark
    grade = ''



grade_no = {'A': 0,
            'B': 0,
            'C': 0,
            'Fail': 0}

student_register = []

no_sutdents = int(input("Enter the number of students: "))

for i in range(no_sutdents):

    name = input("Enter the name: ")
    mark = int(input('Enter the Mark: '))
    student = students(name,mark)

    if student.marks >= 90:

        student.grade = 'A'
        print(f"Grade: A")
        grade_no ['A'] += 1

    elif student.marks >= 75 and student.marks <= 89:

        student.grade = 'B'
        grade_no['B'] += 1
        print(f"Grade: B")

    elif student.marks >= 50 and student.marks <= 74:

        student.grade = 'C'
        grade_no['C'] += 1
        print("Grade: C")

    elif student.marks < 50:

        grade_no ['Fail'] += 1
        student.grade = 'Fail'
        print("Fail")

    student_register.append(student)
    
    print()

for grad in student_register:
    print(f"Name: {grad.name}")
    print(f"Mark: {grad.marks}")
    print(f"Grade: {grad.grade}")
    print()

print(grade_no)
print()