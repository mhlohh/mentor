import sys
class house:
    def __init__(self,name,liters):
        self.liters= liters
    usage = ''

house_list = []

usage_dict = {"Normal usage" : 0,
                 "High usage" : 0,
                 "Execess usage": 0}

numberHouses = int(input("Enter the number of Houses(Max 10): "))

if numberHouses > 10 and numberHouses < 1:
    print("Invalid Input!!❌")
    sys.exit()

for i in range(numberHouses):

    name = input("Enter the House name: ")
    liter = int(input("Enter the liter of water: "))

    water = house(name,liter)

    print()

    if water.liters <= 200:
        water.usage = 'Normal usage'
        usage_dict[water.usage] += 1
        print(water.usage)
        

    elif water.liters < 200 and water.liters <= 400:
        water.usage = 'High usage'
        usage_dict[water.usage] += 1
        print(water.usage)

    elif water.liters > 400:
        water.usage = 'Excess usage'
        usage_dict[water.usage] += 1
        print(water.usage)

    print()
    house_list.append(water)


for std in house_list:
    print(f"House Name: {std.name}")
    print(f"Liter: {std.liters}")
    print(f"Usange: {std.usage}")
    print()

print(usage_dict)