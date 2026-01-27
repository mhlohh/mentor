import sys
class User:
    def __init__(self,name,data):
        self.name = name
        self.data = data
    
    warnings = ''

user_list = []

user_dict = {"Normal" : 0,
                 "Warning" : 0,
                 "Extra charges": 0
            }

numberUser = int(input("Enter the number of Costumer(Max 10): "))

if numberUser > 10 and numberUser < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberUser):

    name = input("Enter the name: ")
    data = int(input("Enter the data usage: "))

    user = User(name,data)

    print()

    if user.data <= 1:

        print("Normal Data usage")
        user.warnings = 'Normal'
        user_dict["Normal"] += 1
        

    elif user.data > 1 and user.data <= 2:

        print("Warning Data usage")
        user.warnings = 'Warning'
        user_dict["Warning"] += 1

    elif user.data > 2:

        print("Extra charges usage")
        user.warnings = 'Extra charges'
        user_dict["Normal"] += 1

    print()
    user_list.append(user)

for std in user_list:
    print(f"Name: {std.name}")
    print(f"Data: {std.data}")
    print(f"Warnings: {std.warnings}")
    print()

print(user_dict)