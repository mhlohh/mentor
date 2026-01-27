import sys
class person:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    Fine = 0

civilian_list = []

fine_list = [500,1000]

totalFine = 0

numberPerson = int(input("Enter the number of People(Max 10): "))

if numberPerson > 10:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberPerson):

    name = input("Enter the name: ")
    speed = int(input("Enter the Speed: "))
    civilian = person(name,speed)

    print()

    if civilian.speed <= 60 :

        print("No fine")
        

    elif civilian.speed >= 61 and civilian.speed <= 80:

        civilian.Fine = fine_list[0]
        print(f"Fine: {civilian.Fine}")
        totalFine += fine_list[0]

    elif civilian.speed > 80:

        civilian.Fine = fine_list[1]
        print(f"Fine: {civilian.Fine}")
        totalFine += fine_list[1]
    print()
    civilian_list.append(civilian)


for std in civilian_list:
    print(f"Name: {std.name}")
    print(f"speed: {std.speed}")
    print(f"Fine: {std.Fine}")
    print()

print(f"Total Fine: {totalFine}")