number = input("Enter the number: ")
sum = 0
i = len(number)
for num in number:
    sum += int(num)**i
if sum == int(number):
    print("Acient Vault is Open !✅")
else:
    print("Wrong Number ❌")