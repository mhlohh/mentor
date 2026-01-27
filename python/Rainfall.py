import sys

no_day = int(input("Enter the number of days: "))

if no_day < 1:
    print("Invalid day")
    sys.exit()

rainfall_dict = {'Low' : 0,
            'Moderate': 0,
            'Heavy':0   
           }

for i in range(no_day):
    rainfall = int(input("Enter the rainfall intensity in mm: "))
    if rainfall < 10:
        rainfall_dict['Low'] += 1
    
    elif rainfall >= 10 and rainfall<=50:
        rainfall_dict['Moderate'] += 1

    elif rainfall > 50:
        rainfall_dict['Heavy'] += 1
print()

print(rainfall_dict)