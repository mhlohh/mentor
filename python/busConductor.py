costPerKm = 5
student_costPerkm = 1
Distance = int(input("Enter the Distance: "))
ticketCharge = 0
age = int(input("Enter the age: "))
if age <= 0 or Distance <= 0:
    print('Invalid input!❌')
elif age <= 5:
    print("Ticket charge free!!🆓")
elif age > 5 and age < 15:
    ticketCharge = student_costPerkm * Distance
    print(f"Cost: {ticketCharge}﹩")
elif age >= 15:
    ticketCharge = costPerKm * Distance
    print(f"Cost: {ticketCharge}﹩")
