import random
import sys
def roll():
    min_value = 1
    max_value= 6
    return random.randint(min_value,max_value)

value = roll()
print(value)
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between(1-4) players")
        
    else:
        print("Invalid, try again.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score ) < max_score:
    
    for i in range(players):
        current_score = 0
        print("\nPlayer", i + 1, "turn has hust started\n")
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ",value)
            
            print(f"Your score is: {current_score}")
        
        player_score[i] += current_score
        print("Your total score is:",player_score[i])
    
        
winner_score = max(player_score)
winning_player_inx = player_score.index(max_score)
print(f"Player {winning_player_inx + 1} \n Wiht Score: {winner_score}")
    
 