import sys
class person:
    def __init__(self,name,hours):
        self.name = name
        self.hours = hours

    overTimepay = 0

employee_list = []

employee_dict = {"No overtime pay" : 0,
                 "overtime 500" : 0,
                 "overtiime 1000": 0
            }

numberEmployee = int(input("Enter the number of Employee(Max 10): "))

if numberEmployee > 10 and numberEmployee < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberEmployee):

    name = input("Enter the name: ")
    hours = int(input("Enter the work hours: "))

    employee = person(name,hours)

    print()

    if employee.hours <= 5:

        print("No overtime pay")
        employee.overTimepay = 0
        employee_dict["No overtime pay"] += 1
        

    elif employee.hours >= 6 and employee.hours <= 10:
        print("Overtime pay: 500")
        employee.overTimepay = 500
        employee_dict["overtime 500"] += 1
        

    elif employee.hours > 10:
        print("Overtime pay: 1000")
        employee.overTimepay = 1000
        employee_dict["overtime 1000"] += 1

    print()
    employee_list.append(employee)

for std in employee_list:
    print(f"Name: {std.name}")
    print(f"Hours: {std.hours}")
    print(f"Overtime Pay: {std.overTimepay}")
    print()

print(employee_dict)