# Write your code here
import random


def intro():
    """Print welcome text."""
    print("H A N G M A N")
    print("The game will be available soon.")


def rand_word():
    """Choose a random word from provided list of words."""
    word_list = ['python', 'java', 'swift', 'javascript']
    choice = random.choice(word_list)
    return choice


# Assign a random word from list to 'word'.
word = rand_word()


def guess_word(provided_word):
    """Compare user input to randomly chosen word."""
    user_guess = input("Guess the word: ")
    if user_guess == provided_word:
        print("You survived!")
    else:
        print("You lost!")


intro()
guess_word(word)
