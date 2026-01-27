class costumer:
    def __init__(self,name,bill):
        self.name = name
        self.bill = bill
    final_amount = 0

costumer_list = []
discount_list = [20,10]
countCostumer = int(input("Enter the number of consumers: "))

for i in range(countCostumer):

    name = input("Enter the name: ")
    
    bill = int(input("Enter the Bill: "))
    print()
    person = costumer(name,bill)

    if person.bill >= 5000:

        person.final_amount = person.bill + ((discount_list[0] * person.bill)/100)
        print(f"Discounted Price:{person.final_amount} 💸")

    elif person.bill >= 2000 and person.bill <= 4999:

        person.final_amount = person.bill + ((discount_list[1] * person.bill)/100)
        print(f"Discounted Price:{person.final_amount} 💸")


    elif person.bill < 2000:
        print("No Discount is available ❌")

    print()
    costumer_list.append(person)

for people in costumer_list:
    print(f"Name: {people.name}")
    print(f"Bill: {people.bill}")
    print(f"Discounted price: {people.final_amount}")
    print()
