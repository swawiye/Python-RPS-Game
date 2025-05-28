print("Welcome to the RPS Game.")
print("Rules")
print("1. Rock defeats Scissors")
print("2. Paper defeats Rock")
print("3. Scissors defeat Paper")

#choice = input()
#
## Variables
#r = "rock"
#p = "paper"
#s = "scissors"
#
## Rock
#if choice == r:
#    print("You chose {choice}. It's a tie.")
#elif choice == s:
#    print("You chose {choice}. You lose.")
#else:
#    print("You chose {choice}. You win!")
#
## Paper
#if choice == p:
#    print("You chose {choice}. It's a tie.")
#elif choice == r:
#    print("You chose {choice}. You lose.")
#else:
#    print("You chose {choice}. You win!")
#    
## Scissors
#if choice == s:
#    print("You chose {choice}. It's a tie.")
#elif choice == r:
#    print("You chose {choice}. You lose.")
#else:
#    print("You chose {choice}. You win!")

import random

options = ("rock", "paper", "scissors")

player = None 
computer = random.choice(options) # pick a random choice from options

while player not in options: # encures that the player only picks one of the presented options
    player = input("Choose your weapon(rock, paper, scissors): ") # player's choice

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie.")
elif player == "rock" and computer == "scissors": # rock winning validation
    print("You win!")
elif player == "paper" and computer == "rock": # paper winning validation
    print("You win!")
elif player == "scissors" and computer == "paper": # scissors winning validation
    print("You win!")
else: 
    print("You lose.") # if none of the above are met

