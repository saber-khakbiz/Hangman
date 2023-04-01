
import random
from hangmanCh import display_hangman as HANGMAN_FIGURES


class Hangman:
    def __init__(self, wordlist):
        self.word = random.choice(wordlist)
        self.remaining_guesses = 6
        self.guessed_letters = set()

    def guess(self, letter):
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.remaining_guesses -= 1

    def get_display(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()

    def get_figure(self):
        return HANGMAN_FIGURES(6 - self.remaining_guesses)

    def is_game_over(self):
        if self.remaining_guesses == 0:
            return True
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            print(self.get_figure())
            print(self.get_display())
            letter = input("Guess a letter: ").lower()
            self.guess(letter)
        print(self.get_figure())
        print(self.get_display())
        if self.remaining_guesses == 0:
            print(f"Sorry, you lost. The word was '{self.word}'.")
        else:
            print("Congratulations, you won!")


class WordList:
    def __init__(self, addr: str):
        self.addr = addr

    def Createlist(self):
        # Example usage
        with open(self.addr) as f:
            line = f.readlines()

        f.close()

        # Remove whitespace from list
        wordlist = [l.strip().lower() for l in line]
        return wordlist


if __name__ == "__main__":
    wordlist = WordList(".//words.txt").Createlist()
    game = Hangman(wordlist)
    game.play()
