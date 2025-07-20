import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

while play_again: 

    player_choice = int(input("Hello\n\nEnter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissors:\n\n"))

    if player_choice < 1 or player_choice > 3:
        sys.exit("You must enter 1, 2 or 3")

    print(f"Your choice is {str(RPS(player_choice)).replace('RPS.', '')}.")

    computer_choice = random.randint(1, 3)

    print(f"Computer choice is {str(RPS(computer_choice)).replace('RPS.', '')}.")
    you_win = "🎉 You win !"
    tie_game = "😊 It's a tie !"
    computer_win = "💻 Computer wins !"


    if player_choice == 1 and computer_choice == 3:
        print(you_win)
    if player_choice == 2 and computer_choice == 1:
        print(you_win)
    if player_choice == 3 and computer_choice == 2:
        print(you_win)
    if player_choice == computer_choice:
        print(tie_game)
    else:
        print(computer_win)

    play_again = input('\nEnter Y to keep playing,\nEnter Q to quit\n\n')

    if play_again.lower() == "y":
        continue
    elif play_again.lower() == 'q':
        sys.exit("Thank you for the game,\nBye 👋 !")
    else:
        play_again = input('\nEnter Y to keep playing,\nEnter Q to quit\n')
        

  
