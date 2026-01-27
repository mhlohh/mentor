number = int(input("Enter the number: "))
reversed = 0
while(number > 0):
    reminder = number%10
    reversed += reminder
    reversed *=10
    number //=10
reversed //=10
print(reversed)