from nim import Nim
from 2048game import *

if __name__ == "__main__":
    print("idk")

print("Welcome to RetroGames!\n")
print("Here are your options:")
print("1:Nim    2: 2048    3: Hangman    4: TicTacToe\n")
print("Type here what game you choose to play!")

def correct_input(chosen_game):
    if chosen_game.isdigit() == False:
        print("Just a digit, please! =((")
        return False

    game_number = int(chosen_game)
    if game_number < 1 and game_number > 4:
        print("You don't want to play anything, do you?")
        return False

    return True


chosen_game = input()

while correct_input(chosen_game) == False:
    chosen_game = input()

game_number = int(chosen_game)

if game_number == 1:
    Nim(3)
elif game_number == 2:
    gamepanel = Board()
    game2048 = Game(gamepanel)
    game2048.start()
