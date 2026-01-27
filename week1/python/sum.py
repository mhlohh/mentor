def sum_numbers(n):
    if n < 1:
        return 0
    return n + sum_numbers(n-1)

print(sum_numbers(50))