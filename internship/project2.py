import random

def valid_number(num):
    if num.isdigit():
        if int(num) >  0:
            return [True, ""]
        else:
            return[False, "Please Input number greater than 0 next time"]
    else:
        return [False, "please type a number next time"]
top_of_range = input("Type a number: ")
isValid = valid_number(top_of_range)
if isValid[0] != True:
    print(isValid[1])
    exit()

top_of_range = int(top_of_range)

random_number = random.randint(0,top_of_range)

guess = 0
while True:
    guess+=1
    guess_number = input("Make a guess: ")
    isValid = valid_number(guess_number)
    if isValid[0] != True:
        print(isValid[1])
        continue
    guess_number = int(guess_number)

    if guess_number == random_number:
        print("You got it!")
        break
    elif guess_number > random_number:
        print("Your were above number")
    elif guess_number < random_number:
        print("Your were below!")


print(f"You got in {guess} guesses!")

    


