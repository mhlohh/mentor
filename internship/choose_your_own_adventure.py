name = input("Type your Name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right? "
).lower()

if (answer == "left"):  
    print()
    answer = input("You come to a river , you can walk around it and swim across? ")
    if answer == "swim":
        print("You swam across and were eaten by alligator!")
    elif answer == "walk":
        print("You wlaked for many miles, ran out of water and lost the game")
elif answer == "right":
    answer = input("You come to bridge, it looks wobbly, do you want to cross it or head back(cross/walk)? ").lower
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You corss the bridge and meet a stranger: ").lower()
        if answer == "yes":
            print("You talk to stranger and they give you gold. You Win").lower()
        elif answer == "no":
            print("You ignore the stranger and they are offende and you are screwed")
else:
    print("Not a valid option. You lose.")

print("Thankyou for playing!")