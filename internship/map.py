from functools import reduce

#Lesson1 Higher Order Function in Python

def apply(func,n):
    return func(n)

def square(n):
    return n*n

print(apply(square,5))

#Second Lesson Anonymous Function(Lmabda Function)

add_ten = lambda x: x + 10

print(add_ten(10))

#Third Lesson Map function to Lambda a list

numbers = [1,2,3,4,5,6]
"""map function maps the lambda to each number in the
numbers list just like react map"""

double_number = list(map(lambda x: x*2,numbers))

print(double_number)

#filter function filter()
even_numbers = list(filter(lambda x: x%2 == 0,numbers))

print(even_numbers)

#soted function

students = [("Anu",85),("Rajul",92),("Meera",78)]
sorted_students = sorted(students,key = lambda x: x[1])
print(sorted_students)

"""Advantages of Lambda Functions
● Short and concise syntax.
● Useful for simple operations.
● Commonly used with map(), filter(), reduce(), and sorted().
● Avoids defining separate functions for one-time use."""

#Reduce Function
#This function iterate throug list and fucntion apply cumulatively like x += list[i]

total = reduce(lambda x,y :x+y,numbers )
print(f"total: {total}")