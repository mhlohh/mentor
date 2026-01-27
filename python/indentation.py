"""Indetation is strict and important in python
1. Without porper indendation the program did not work 
2. It help with the cleaniness of the code which the python is really good at
Eg: """

def printPyramid(n):
    for i in range(1,n):
        print("#"*i)

printPyramid(8)

"""In here the progromm doesn't wrok if the space between the user defined function new line gives four spaces the
the function code itself shows syntax error"""

# ERROR
for i in range(5):
print(i)