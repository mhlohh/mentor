import sys
class constumer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    concession = 0

constumer_list = []

constumer_dict = {"50 concession" : 0,
                 "25 concession" : 0,
                 "No concession": 0
            }

numberCostumer = int(input("Enter the number of Costumer(Max 10): "))

if numberCostumer > 10 and numberCostumer < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberCostumer):

    name = input("Enter the name: ")
    age = int(input("Enter the age: "))

    person = constumer(name,age)

    print()

    if person.age < 18:

        person.concession = '50 concession'
        constumer_dict["50 concession"] += 1
        print("50 concession")
        

    elif person.age >= 18 and person.age <= 25:

        person.concession = '25 concession'
        constumer_dict["25 concession"] += 1
        print("25 concession")

    elif person.age > 25:
        person.concession = 'No concession'
        constumer_dict["No concession"] += 1
        print("No concession")

    print()
    constumer_list.append(person)

for std in constumer_list:
    print(f"Name: {std.name}")
    print(f"Age: {std.age}")
    print(f"Concession %: {std.concession}")
    print()

print(constumer_dict)