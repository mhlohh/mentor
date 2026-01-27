number = input("Enter the number: ")
value = False
for i in number:
    if i.isdigit():
        value = True
    else:
        value = False
        break
        
if value == True:
    print("The number is numeric")
else:
    print("This number is not numeric")

print(2*3**2**2)