print("Welcome to my game!")
playing = input("Do you want to play?(yes/no) ")
if playing != "yes":
    exit()

print("Lets start the game!")
print()
Questions = {"What does CPU stand for? ": "central processing unit",
             "What does GPU stand for? " : "graphics processing unit",
             "What does Ram stands for? " : "random acess memory",
             "What does PSU stands for> " : "power supply"
             }
totalScore = len(Questions)
score = 0


for index, (key, value) in enumerate(Questions.items()):
    answer = input(key)
    if (answer == value):
        print("Correct!☑️\n")
        score += 1
    else:
        print("Incorrect!❌\n")

print("-----Score-----\n")
print(f"  *   (Outof: {totalScore}/Score: {score})")
print(f"  *   (Percentage: ({(score / totalScore)*100}))%\n")
