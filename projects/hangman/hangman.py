import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |  
           |
           |
        """,
        """
           -----
           |   |
           |  
           |  
           |
           |
        """,
        """
           -----
           |   
           |  
           |  
           |
           |
        """
    ]
▋

