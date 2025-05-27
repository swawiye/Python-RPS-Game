print("Welcome to the RPS Game. Choose either rock, paper, or scissors")

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
