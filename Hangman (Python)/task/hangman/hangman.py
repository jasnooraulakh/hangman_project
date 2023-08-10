# Write your code here
import random


def intro():
    """Print welcome text."""
    print("H A N G M A N ")
    # print("The game will be available soon.")


# intro()


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


def check_input(user_input):
    """Check the user guess, if it is a single, lowercase alphabet."""
    if user_input == "":
        print("Please, input a single letter.")
        is_valid = False
    else:
        if user_input.isalpha():
            if user_input.islower():
                if int(len(user_input)) < 2:
                    pass
                    is_valid = True
                else:
                    print("Please, input a single letter.")
                    is_valid = False
            else:
                print("Please, enter a lowercase letter from the English alphabet.")
                is_valid = False
        else:
            print("Please, enter a lowercase letter from the English alphabet.")
            is_valid = False
    return is_valid


GAMES_WON = 0
GAMES_LOST = 0


def guess_word(provided_word):
    """Compare user input to randomly chosen word, and reveal guessed letters."""
    i = 8
    hint = user_hint(word)
    guessed_letters = set()

    while i > 0:
        print(hint)
        user_guess = input("Input a letter: ")
        valid_input = check_input(user_guess)

        global GAMES_WON
        global GAMES_LOST

        if not valid_input:
            print()
            continue
        else:

            if user_guess in guessed_letters:
                print("You've already guessed this letter.")
            else:
                guessed_letters.add(user_guess)

                if user_guess not in provided_word:
                    print("That letter doesn't appear in the word.")
                    i -= 1

                else:
                    hint_list = list(hint)
                    for letter in range(len(provided_word)):
                        if provided_word[letter] == user_guess:
                            hint_list[letter] = user_guess
                    hint = "".join(hint_list)

                    if hint == provided_word:
                        print(f"You guessed the word {provided_word}!")
                        print("You survived!")
                        GAMES_WON += 1
                        break

        print()
        if i == 0:
            print("You lost!")
            GAMES_LOST += 1


def game_op():
    intro()
    while True:
        player_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

        if player_choice == 'play':
            # word = rand_word()
            print()
            guess_word(word)
            continue
        elif player_choice == 'results':
            print(f"You won: {GAMES_WON} times.")
            print(f"You lost: {GAMES_LOST} times.")
            continue
        elif player_choice == 'exit':
            exit()


# guess_word(word)
game_op()
