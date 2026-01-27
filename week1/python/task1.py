day = int(input("Enter the number: "))
leaves = 0
day1 = 1
day2 = 1
for i in range(day+1):
      leaves = day1 + day2
      print(f"Days: {leaves}")
      day1 = day2
      day2 = leaves

print(leaves)
        
