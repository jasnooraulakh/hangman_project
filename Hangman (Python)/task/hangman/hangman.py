# Write your code here
import random


def intro():
    """Print welcome text."""
    print("H A N G M A N \n")
    # print("The game will be available soon.")


intro()


def rand_word():
    """Choose a random word from provided list of words."""
    word_list = ['python', 'java', 'swift', 'javascript']
    choice = random.choice(word_list)
    return choice


# Assign a random word from list to 'word'.
word = rand_word()


def user_hint(chosen_word):
    """Show the word length in '-' as a hint."""
    hidden_word = len(chosen_word) * '-'
    return hidden_word


def guess_word(provided_word):
    """Compare user input to randomly chosen word, and reveal guessed letters."""
    i = 0
    hint = user_hint(word)

    while i < 8:
        print(hint)
        user_guess = input("Input a letter: ")
        if user_guess not in provided_word:
            print("That letter doesn't appear in the word.")

        else:
            hint_list = list(hint)
            for letter in range(len(provided_word)):
                if provided_word[letter] == user_guess:
                    hint_list[letter] = user_guess
            hint = "".join(hint_list)
        i += 1
        print()


guess_word(word)
print("Thanks for playing!")
