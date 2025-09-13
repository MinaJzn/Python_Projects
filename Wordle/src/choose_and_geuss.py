import random

with open(r"D:\Python\My_Exercise_Or_My_Project\Wordle\src\valid-wordle-words.txt",'r') as file:
    valid_word=[line.strip() for line in file]


def computer_word()-> dict:
    """Selects a random 5-letter word from the valid words list.
    
    Returns:Contains the random word as a string and a list of its characters.
    """
    random_word=random.choice(valid_word)
    random_word_list=list(random_word)
    random.seed(1)
    return {'random_word':random_word,'random_word_list':random_word_list}


def guess_word()-> dict:
    """Prompts the user to input a 5-letter word as a guess.

    Returns:Contains the guessed word and a list of its characters.
    """
    while True:
        your_word=input('Write your guess:').lower()
        if len(your_word)==5:
            your_word_list=list(your_word)
            return {'your_word':your_word,'your_word_list':your_word_list}
        print('‼️ Please write the word with 5 characters!')
        continue