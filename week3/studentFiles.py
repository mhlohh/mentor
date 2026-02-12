import csv
import os

class students:
    def __init__(self,list):
        self.students_list = list
        self.valid = 0
        self.non_valid = 0
        self.validity_count()

    def validity(self,student):
        if student["mark"].isdigit() and int(student['mark'])<= 100 and int(student['mark']) >= 0:
            return True
        else:
            return False
        
    def validity_count(self):        
        for student in self.students_list:
            if self.validity(student):
                self.valid += 1
        else:
            self.non_valid +=1

    def print_Students(self):
        for student in self.students_list:
            if self.validity(student):
                print(f"Name {student["name"]}\t Marks: {student["mark"]}\n")
            else:
                print(f"Name {student["name"]}\t Marks Invalid\n")

    def students_average(self):
        sum  = 0
        for student in self.students_list:
            if self.validity(student):
                sum += int(student['mark'])
            
        avg = sum/len(self.students_list)
        return avg

    
 

    

filename = "studentFile.csv"
student_list = []
try:

    if os.path.isfile(filename):

        print("Your file exist !")

    else:

        raise ValueError("The File doesn't exist")
    
    with open(filename,mode = 'r')as file:

        csv_reader = csv.DictReader(file)
        for row in csv_reader:

            student_list.append(row)

    s = students(student_list)

    print("Print Studnets[1]\tPrintValidity[2]\tStudents Average Marks[3]")
    x = int(input("Instruction: "))
    if x == 1:
        s.print_Students()
    elif x == 2:
        print(f"Valid: {s.valid}")
        print(f"Non Valid: {s.non_valid}")
    elif x == 3:
        print(f"Average Mark = {s.students_average()}")
        
except ValueError as e:
    print(e)






