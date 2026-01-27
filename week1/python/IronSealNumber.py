numbers = input("Enter the number: ")
sum_c = 1
sum = 0
for i in numbers:
    for num in i:
        sum_c *= int(num)
    sum += sum_c
    sum_c = 1
if sum == sum_c:
    print("Iron gate is Open ✅")
else:
    print("Seal number is wrong ❌")
