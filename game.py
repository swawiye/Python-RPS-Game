print("Welcome to the RPS Game.")
print("Rules")
print("1. Rock defeats Scissors")
print("2. Paper defeats Rock")
print("3. Scissors defeat Paper")

import random

options = ("rock", "paper", "scissors")

running = True # the game running, makes the boolean easier to use in larger code

while running: # creates a loop to enables continuous playing
    # Reset the player choices and the computer choices
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

    # Exiting the loop
    play_again = input("Play again? (y/n): ").lower() # temporary variable that asses whether the player would like to play again, "lower()" method converts the string into lowercase letters
    if not play_again == "y": # if the user doesn't want to play again, escape the loop
        running = False

print("Thanks for playing!")

# Alternative method for exiting the loop
#if not input("Play again? (y/n): ").lower() == "y":
#    running = False

