from random import randint

def compare(user, computer):
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
    choices = ['Rock', 'Paper', 'Scissors']
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice

def game_loop():
    play_game = True

    while play_game:
        user = input("Rock, paper or scissors?")
        computer = get_computers_choice()

        victor = compare(user, computer)

        play_again = input("Would you like to play again: Y/N?")

        if play_again.lower() == 'n':
            play_game = False

    print("Thanks for playing!")

game_loop()