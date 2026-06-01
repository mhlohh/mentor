import random

user_score = 0
computer_score = 0

option = ["rock","sissor","paper"]

while True:
    user_input = input("Rock/Paper/Sissor/Q: ").lower()

    if user_input == 'q':
        break

    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    computer_pick = option[random_number]
    print(f"Computer Picked: {computer_pick}")
    if user_input == computer_pick:
        print("Tie!")
    elif user_input == option[0] and computer_pick == option[1]:
        print("User Get Point")
        user_score += 1
    elif user_input == option[0] and computer_pick == option[2]:
        print("Computer Get Point!")
        computer_score += 1
    elif user_input == option[1] and computer_pick == option[0]:
        computer_score += 1
        print("Computer get Score")
    elif user_input == option[1] and computer_pick == option[2]:
        user_score += 1
        print("User get Score")
    elif user_input == option[2] and computer_pick == option[0]:
        user_score += 1
        print("User get Score")
    elif user_input == option[2] and computer_pick == option[1]:
        computer_score += 1
        print("Computer get Score")
print()
print("-----Score----")
print(f"User Scor: {user_score}")
print(f"Computer Scroe: {computer_score}\n")
if computer_score > user_score:
    print("Computer Wins!\n")
elif user_score > computer_score:
    print("User Wins\n")
else:
    print("Tie !")