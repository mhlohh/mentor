import random
import string

def generate_password(min_length, numbers = True,special_charecter = True):
    letters = string.ascii_letters
    digit = string.digits
    special = string.punctuation
    charecters = letters
    if numbers:
        charecters += digit
    if special_charecter:
        charecters += special
    
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(charecters)
        pwd += new_char
        
        if new_char in digit:
            has_number = True
        if new_char in special:
            has_special = True
            
        meet_criteria = True
        
        if numbers:
            meet_criteria = has_number
        if special_charecter:
            meet_criteria = meet_criteria and has_special
    return pwd
        
        
minLengt = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers(y/n)? ").lower()
has_special = input("Do you want to have Special char (y/n)? ").lower()

if has_number == 'n':
    has_number = bool(False)
if has_special == 'n':
    has_special = bool(False)
print(generate_password(minLengt,has_number,has_special))