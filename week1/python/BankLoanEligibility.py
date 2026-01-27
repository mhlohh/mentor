import sys
class costumer:
    def __init__(self,name,income):
        self.name = name
        self.income = income
    
    eligibilty = ''

costumer_list = []

loan_dict = {"High Loan" : 0,
                 "Medium Loan" : 0,
                 "Not Eligible": 0
            }

numberCostumer = int(input("Enter the number of Costumer(Max 10): "))

if numberCostumer > 10 and numberCostumer < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberCostumer):

    name = input("Enter the name: ")
    income = int(input("Enter the Income "))

    person = costumer(name,income)

    print()

    if person.income >= 500000:

        print("High Loan ✅")
        person.eligibilty = 'Full Fee'
        loan_dict["High Loan"] += 1
        

    elif person.income >= 300000 and person.income <= 499999:
        
        print("Medium Loan ✅")
        person.eligibilty = 'Medium Loan'
        loan_dict["Medium Loan"] += 1

    elif person.income < 300000:

        print("Not Eligible ❌")
        person.eligibilty = 'Not elgible'
        loan_dict["Not Eligible"] += 1
    print()
    costumer_list.append(person)

for std in costumer_list:
    print(f"Name: {std.name}")
    print(f"speed: {std.income}")
    print(f"Fine: {std.eligibilty}")
    print()

print(loan_dict)