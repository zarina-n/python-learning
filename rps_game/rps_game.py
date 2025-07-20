import sys
import random
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    player_choice = int(input("\n\nEnter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissors:\n\n"))

    if player_choice not in [1, 2, 3]:
        print("You must enter 1, 2 or 3\n\n")
        return play_rps()

    computer_choice = random.randint(1, 3)

    print(f"Your choice is {str(RPS(player_choice)).replace('RPS.', '')}.")
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

  
    while True:
        players_answer = input('\nEnter Y to keep playing,\nEnter Q to quit\n\n')
        if players_answer.lower() not in ['y', 'q']:
            continue
        else:
            break

    if players_answer.lower() == "y":
        return play_rps()
    else:
        sys.exit("\nThank you for the game,\nBye 👋 !")
  
            

  
play_rps()
