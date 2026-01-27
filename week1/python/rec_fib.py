def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

limit = int(input("Enter the number: "))
for i in range(limit):
    print(fibonacci(i),end = " ")
print()