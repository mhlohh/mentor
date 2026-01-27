number = input("Enter the number: ")
limit = 0
sum = 0
while(limit != 1):
    sum = 0
    for num in number:
        sum += int(num)
    number = str(sum)
    limit = len(str(sum))
if sum == 1:
    print("The scroll accept ✅")
else:
    print("The scroll reject ❌")
