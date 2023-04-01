import random

class Hangman:
    
    def __init__(self, wordlist, difficulty='normal'):
        self.word = random.choice(wordlist)
        if difficulty == 'easy':
            self.remaining_guesses = 8
        elif difficulty == 'hard':
            self.remaining_guesses = 4
        else:
            self.remaining_guesses = 6
        self.guessed_letters = set()

    def guess(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
        elif letter in self.word:
            self.guessed_letters.add(letter)
            print("Correct!")
        else:
            self.guessed_letters.add(letter)
            self.remaining_guesses -= 1
            print("Incorrect.")
        self.display()

    def display(self):
        print(f"Word: {' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)}")
        print(f"Incorrect guesses: {' '.join(sorted(self.guessed_letters - set(self.word)))}")
        print(f"Remaining guesses: {self.remaining_guesses}")


    def is_game_over(self):
        return self.remaining_guesses == 0 or set(self.word) == self.guessed_letters

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            letter = input("Guess a letter: ").lower()
            self.guess(letter)
        if self.remaining_guesses == 0:
            print(f"Sorry, you lost. The word was '{self.word}'.")
        else:
            print("Congratulations, you won!")

class WordList:
    def __init__(self,addr:str):
        self.addr = addr
    
    def Createlist(self):
        # Example usage
        with open(self.addr) as f:
            line = f.readlines()

        f.close()

        # Remove whitespace from list
        wordlist = [l.strip().lower() for l in line]
        return wordlist

wordlist = WordList(".//words.txt").Createlist()
game = Hangman(wordlist, "hard")
game.play()
