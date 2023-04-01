# The function of displaying the character of Hangman at each stage of the game


def display_hangman(incorrect_guesses):
    stages = [
        '''
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                  =========
    ''',
        '''
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                  =========
    ''',
        '''
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                  =========
    ''',
        '''
                    +---+
                    |   |
                    O   |
                   /|   |
                        |
                        |
                  =========
    ''',
        '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                  =========
    ''',
        '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                  =========
    ''',
        '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                 ===Dead=== 
    ''',
    ]
    return stages[incorrect_guesses]
