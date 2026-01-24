import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_games = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie_games

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = int(input("\n\nEnter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissors:\n\n"))

        if player_choice not in [1, 2, 3]:
            print("You must enter 1, 2 or 3\n\n")
            return play_rps()

        computer_choice = random.randint(1, 3)

        print(f"\nYour choice is {str(RPS(player_choice)).replace('RPS.', '')}.\n")
        print(f"Computer choice is {str(RPS(computer_choice)).replace('RPS.', '')}.\n")

    
        def get_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie_games

            you_win = "🎉 YOU WIN !"
            tie_game = "😊 IT'S A TI !"
            computer_win = "💻 COMPUTER WINS !"

            if player_choice == 1 and computer_choice == 3:
                player_wins += 1
                return you_win
            if player_choice == 2 and computer_choice == 1:
                player_wins += 1
                return you_win
            if player_choice == 3 and computer_choice == 2:
                player_wins += 1
                return you_win
            if player_choice == computer_choice:
                tie_games += 1
                return tie_game
            else:
                computer_wins += 1
                return computer_win

        game_result = get_winner(player_choice, computer_choice)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print('_____________________')
        print(f"\nTie games: {tie_games}")
        print('_____________________')
        print(f"\nYour wins: {player_wins}")
        print('_____________________')
        print(f"\nComputer wins: {computer_wins}")
        print('_____________________')

    
        while True:
            players_answer = input('\nEnter Y to keep playing,\nEnter Q to quit\n')
            if players_answer.lower() not in ['y', 'q']:
                continue
            else:
                break
    
        if players_answer.lower() == "y":
            return play_rps()
        else:
            sys.exit("\nThank you for the game,\nBye 👋 !")

        
    return play_rps
    
            

  
play = rps()

play()
