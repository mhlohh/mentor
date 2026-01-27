class employees:
    def __init__(self,name,years):
        self.name = name
        self.years = years
    bonus = 0

employee_list = []
years_list = [5,10,20]
n_emplyee = int(input("Enter the number of consumers: "))

for i in range(n_emplyee):

    name = input("Enter the name: ")
    
    year = int(input("Enter the no of years: "))
    person = employees(name,year)

    if person.years < 5:

        person.bonus = person.years * years_list[0]
        print(f"Bonus :{person.bonus}")

    elif person.years >= 5 and person.years <= 9:

        person.bonus = person.years * years_list[1]
        print(f"Bonus :{person.bonus}")

    elif person.years >= 10:

        person.bonus = person.years * years_list[2]
        print(f"Bonus :{person.bonus}")

    print()
    employee_list.append(person)

for people in employee_list:
    print(people.name)
    print(people.bonus)
    print()
