def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

number = input("Enter the number: ")
sum =0
for i in number:
    sum += factorial(int(i)) 
if sum == int(number):
    print("This number is strong number")
else:
    print("This number is not strong number")