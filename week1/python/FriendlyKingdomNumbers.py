def kingdomNumber(num):
    sum = 0
    for i in range(1,num):
       if num % i == 0:
           sum += i

    return sum


number1 = int(input("Enter the First Number number: "))
number2 = int(input("Enter the Second Number number: "))
sum_number1 = kingdomNumber(number1)
sum_number2 = kingdomNumber(number2)
if sum_number1 == sum_number2:
    print("The number is friendly ✅")
else:
    print("The number is not friendly ❌")