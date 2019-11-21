"""
A rock, paper, scissors game written in Python

Origional Author: The Code Institute Learning Team
"""
from random import randint

def compare(user, computer):
    """
    Compare the user's and computer's selections to determine the
    winner of the game.

    We use an if-else ladder to check the rules of the user's selection
    and then compare it to the computer's selection.

    We use the .lower() string method to ensure that each of the choices that we're
    checking for are lowercase. This will ensure that the values on both sides of the condition
    are lowercase.

    """

    if user.lower() == computer.lower():
        print("It's a tie!")
    elif user.lower() == 'rock':
        if computer.lower() == 'scissors':
            print("You win!")
        else:
            print("The Computer wins")
    elif user.lower() == 'scissors':
        if computer.lower() == 'paper':
            print("You win!")
        else:
            print("The Computer wins")
    elif user.lower() == 'paper':
        if computer.lower() == 'rock':
            print("You win!")
        else:
            print("The Computer wins")
    else:
        print("Invalid input! You have not entered Rock, Paper or Scissors. Please try again.")

def get_computers_choice():
    """
    Generate a random selection for the computer based on the three available
    selections: Rock, Paper and Scissors.

    Return the choice so it can be stored in memory as the computer's selection
    """
    choices = ['Rock', 'Paper', 'Scissors']
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice

def game_loop():
    """
    This is our main game loop. This code will
    run the game until the user explictly decides to
    quit.
    """
    play_game = True

    while play_game:
        user = input("Rock, paper or scissors?").lower()
        computer = get_computers_choice().lower()

        compare(user, computer)

        play_again = input("Would you like to play again: Y/N?")

        if play_again.lower() == 'n':
            play_game = False

    print("Thanks for playing!")

# Invoke the game_loop function to start the game
game_loop()