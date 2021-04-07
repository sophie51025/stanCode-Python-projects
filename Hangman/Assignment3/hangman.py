"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    The program plays hangman game. user has N_TURNS chance of guessing wrong.
    """
    word = random_word()
    initial_format = '-' * len(word)
    print('The word looks like: ' + initial_format)
    print('You have ' + str(N_TURNS) + ' guesses left.')

    missing_letters = len(word)

    left = N_TURNS
    while True:
        guessing = ''  # The word includes guessed letters and missing letters
        guess = input('Your guess: ')
        guess = guess.upper()
        if not guess.isalpha():
            print('illegal format.')
        elif len(guess) != 1:
            print('illegal format.')
        elif initial_format.find(guess) != -1:
            print('You are correct!')
        else:
            for i in range(len(word)):
                ch = word[i]
                if ch == guess:
                    missing_letters -= 1
                    guessing += ch
                else:
                    guessing += initial_format[i]
            if guessing == initial_format:
                left -= 1
                print('There is no ' + guess + ' \'s in the word.')
            else:
                initial_format = guessing
                print('You are correct!')
        if left == 0:
            print('You are completely hung :( ')
            print('The word was: ' + word)
            return
        elif missing_letters == 0:
            print('You WIN !!! ')
            print('The word was: ' + word)
            return
        print('The word looks like: ' + initial_format)
        print('You have ' + str(left) + ' guesses left.')

def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
