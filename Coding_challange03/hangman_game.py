# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist
    
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    return random.choice(all_words)


# end of helper code
# -----------------------------------


def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    # TODO: Fill in your code here
    count = 0
    try:
        with open(WORDLIST_FILENAME,'r') as f:
            print("Loading Word List from file: words.txt")
            for words in f:
                count += len(words.strip())       
        return count         
                   
                
    except FileNotFoundError:
        print("File not found!")
                    


# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function

# wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    # TODO: Fill in your the code here
    letter_guessed = set(letters_guessed)
    words = set(word)
    if words.issubset(letter_guessed):
        return True
    else:
        return False
            
        
    


def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    result = []
    # TODO: Fill in your code here
    for letter in word:
        if letter in set(letters_guessed):
            result.append(letter)
        else:
            result.append('_') 
    return ''.join(result)            
            
    
    


def get_remaining_letters(letters_guessed):
    
#     Step 2 – Identifying Unused Letters:
# Implementation Details:
# Your next task is to implement the get_remaining_letters function. This will be used to
# generate a string of letters that have not yet been guessed. The function takes a single argument
# letters_guessed, a list of letters (strings) that the user has previously guessed. You will
# need to write additional code to compare these letters against the full alphabet to determine the
# letters that remain and return them as a string.
# Hint: You may find the string.ascii_lowercase variable useful, which generates a list
# of alphabetical letters in lowercase. The string library has been imported for you.
 new_list_asciii = []
 from string import ascii_lowercase
 new_words = set(letters_guessed)
 for letters in ascii_lowercase:
     if letters not in new_words:
         new_list_asciii.append(letters)
 return new_list_asciii        
              
         
     
 
 
 
# abcdefghijklmnopqrstuvwxyz # All lowercase letters

# Example Usage:
# >>> letters_guessed = ['a', 'e', 'c']
# >>> print(get_remaining_letters(letters_guessed))
# bdfghijklmnopqrstuvwxyz # Letters minus letters_guessed
    
    
    
    
"""
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here
pass

def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    print("-------------")
    # TODO: Fill in your code here


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    result = load_words()
    print(result)
    letter_guessed = ['m','a','l','l','u','a']
    letterss = get_remaining_letters(letter_guessed)
    print(letterss)
    
    guessed_word = is_word_guessed('malla',letter_guessed)
    print(guessed_word)
    
    get_guessed = get_guessed_word('majla', letter_guessed)
    print(get_guessed)
    # Uncomment the line below once you have finished testing.
    # word = choose_random_word(wordlist)

    # Uncomment the line below once you have implemented the hangman function.
    # hangman(word)
    pass