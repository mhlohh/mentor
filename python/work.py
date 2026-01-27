str_number = "50"  # string
int_number = 10    # integer

# Explicitly convert the string to an integer before addition
result = int(str_number) + int_number

print(result)
print(type(result))
# Output:
# 60
# <class 'int'>

float_number = 10.4
#Implecitley convert the int to float for better compatiblity
result = int_number + float_number
print(result)
print(type(result))
# Output: 
# 20.4
# <class 'float'>

#Literals are the values that doesn't change of run time of the program
#Eg: 
literal = 45
#this value is fixed in the source code it is not changing anywhere