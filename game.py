print("Welcome to the RPS Game. Choose either rock, paper, or scissors")
print("Rules")
print("1. Rock defeats Scissors")
print("2. Paper defeats Rock")
print("3. Scissors defeat Paper")

choice = input("Choose your weapon:")

# Variables
r = "rock"
p = "paper"
s = "scissors"

# Rock
if choice == r:
    print("You chose {choice}. It's a tie.")
elif choice == s:
    print("You chose {choice}. You lose.")
else:
    print("You chose {choice}. You win!")

# Paper
if choice == p:
    print("You chose {choice}. It's a tie.")
elif choice == r:
    print("You chose {choice}. You lose.")
else:
    print("You chose {choice}. You win!")
    
# Scissors
if choice == s:
    print("You chose {choice}. It's a tie.")
elif choice == r:
    print("You chose {choice}. You lose.")
else:
    print("You chose {choice}. You win!")

import random

options = ("rock", "paper", "scissors")
player = None 
computer = random.choice(options) # pick a random choice from options

