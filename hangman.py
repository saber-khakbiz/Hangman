import random
import time
from hangmanCh import display_hangman
# Open and Read List of words used in the game

with open(".//words.txt") as f:
    line = f.readlines()

f.close()

# Remove whitespace from list

words_list = [l.strip().lower() for l in line]


# Random word selection function

def get_word():
    return random.choice(words_list)

# The function of displaying the word in the current state with the letters guessed by the player


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
        displayed_word += " "
    return displayed_word

# Function to check the letter guessed by the player


def check_letter(word, guessed_letters, letter):
    if letter in guessed_letters:
        print("This word has already been guessed!")
        return False
    guessed_letters.append(letter)
    if letter in word:
        return True
    else:
        return False

# Function to check remaining time of game


def remain_time(start_time):
    elapsed_time = time.time() - start_time
    remaining_time = max(60 - int(elapsed_time), 0)
    print("Remaining time is:", remaining_time, "seconds")
    return remaining_time


# Function to run the game


def play_game():
    # Random word selection
    word = get_word()
    # Game start mode
    guessed_letters = []
    incorrect_guesses = 0
    # Set of letter numbers
    start_time = time.time()
    while incorrect_guesses < 6:
        # remaining time of game
        remaining_time = remain_time(start_time)
        # Display the word with guessed letters
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)
        # Show the Hangman character in each stage
        print(display_hangman(incorrect_guesses))
        # Check game status
        if "_" not in displayed_word:
            print("congratulations! You guessed the word :))\n\n")
            return
        # Request the guessed word from the player
        guess = input("Guess one letter of the word:")
        # Check remaining time of game
        if remaining_time == 0:
            print("Game Time is over !!!")
            break
        # Check the letter guessed by the player
        if check_letter(word, guessed_letters, guess):
            print("The letter is correct.")
        else:
            print("The letter is incorrect!")
            incorrect_guesses += 1

    print("Unfortunately, you lost. The correct word was {} :((".format(word))
    print(display_hangman(-1),)


if __name__ == "__main__":
    play_game()
