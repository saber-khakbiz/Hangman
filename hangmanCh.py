# The function of displaying the character of Hangman at each stage of the game


def display_hangman(incorrect_guesses):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |      
                   -
                """,
        """
                   --------
                   |      |
                   |      
                   |  < You Lose! >
                   |      
                   |      
                   -
                """
    ]
    return stages[incorrect_guesses]
