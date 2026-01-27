series = [0,1]
current = 0
limit = int(input("Enter the number: "))
i = 0
while (current < limit ):
    current = series[i] + series[i+1]
    series.append(current)
    i+= 1
print(series)