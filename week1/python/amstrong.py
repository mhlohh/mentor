def amstrong(n):
    sum = 0
    for i in n:
        sum += int(i)**3
    if sum == int(n):
        return True
    else:
        return False

number = input("Enter the number: ")
if amstrong(number):
    print("This number is amstrong number")
else:
    print("This number is not amstrong nuber")
