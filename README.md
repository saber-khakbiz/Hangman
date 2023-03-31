# Hangman Game in Python

![Hangman Game in Python](hangman.png)

This is a simple command-line implementation of the classic game of Hangman, written in Python.

## How to Play

The objective of the game is to guess a word by suggesting letters. The game starts by choosing a random word from a list of words, and displaying the number of letters in the word as underscores. The player has to guess the letters in the word one by one. For every incorrect guess, a part of the hangman's body is drawn. The game ends either when the player correctly guesses the word or when the hangman is completely drawn.

To play the game, simply run the `hangman.py` script in a Python environment. You will be prompted to input a letter each turn, and the game will display the current state of the word and the hangman. You can input a letter by typing it and pressing enter.

## Requirements

The Hangman game requires Python 3.x to be installed on your system. No additional libraries or packages are required.

## File Structure

The project contains the following files:

- `hangman.py` - the main script to run the game
- `words.txt` - a text file containing a list of words that the game chooses from
- `README.md` - this file

## Contribution Guidelines

Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

This project was inspired by the classic game of Hangman, and was created as a personal project to practice Python programming.
