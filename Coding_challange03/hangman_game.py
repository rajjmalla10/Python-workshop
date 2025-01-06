# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

from string import ascii_lowercase

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
    try: 
        
        return random.choice(all_words)  
    except ValueError:
        print("No words were found in the word list. The fuke us empty")
    except Exception as e:
        print(f"An unexpected error occured{e}")    
     
            
            
                    
            
    


# end of helper code
# -----------------------------------


def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    
    wordlist = []
    # TODO: Fill in your code here
    count = 0
    
    try:
        with open(WORDLIST_FILENAME,'r') as f:
            print("\nLoading Word List from file: words.txt")
            for line in f:
                words = line.strip().split()
                wordlist.extend(words) 
                count += len(words)       
        print(f'{count} words loaded') 
        return wordlist
           
             
                   
                
    except FileNotFoundError:
        print("File not found!")
        return []
                    


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
    if letter_guessed == word:
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
            
    
    


def get_remaining_letters(letters_guessed=None):
    
    if letters_guessed is None:
        letters_guessed= []
    
    remaning_char = ''.join(sorted(set(ascii_lowercase) - set(letters_guessed)))
    return remaning_char
    
#     Step 2 – Identifying Unused Letters:
# Implementation Details:
# Your next task is to implement the get_remaining_letters function. This will be used to
# generate a string of letters that have not yet been guessed. The function takes a single argument
# letters_guessed, a list of letters (strings) that the user has previously guessed. You will
# need to write additional code to compare these letters against the full alphabet to determine the
# letters that remain and return them as a string.
# Hint: You may find the string.ascii_lowercase variable useful, which generates a list
# of alphabetical letters in lowercase. The string library has been imported for you.

 
 
 
 
    
              
 
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
    guess = 6
    letters_guessed = []
    
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    print("Welcome to Hangman Ultimate Edition")
    print(f"I am thinking of a word that is {len(word)} letters long")
    print("-------------")
    # TODO: Fill in your code here
    letter_guessed = ''
    
    try: 
        while guess > 0:
            print(f"\nYou have {guess} guesses left. ")
            print(f"Avilable letters:{get_remaining_letters(letter_guessed)}")
            letter_guessed = input("Please guess a letter: ")
            
            while len(letter_guessed) > 1 or not letter_guessed.isalpha():
                guess -= 1
                letter_guessed = input("Please enter a valid Guess only a letter, Try again: ")
                
                if guess < 1:
                    print(f"Sorry!!,You have {guess} guesses left.")
                    break
            
            if letter_guessed in letters_guessed:
                guess -= 1
                print(f"Oops! You've already guessed that letter: {letter_guessed}")
                continue
            letters_guessed.append(letter_guessed)
                 
            
            
            
            
            
                
            if letter_guessed in word:
                result = get_guessed_word(word, letters_guessed)
                print(f'Good Guess: {result}')
                print("-------------")   
            else:
                guess -= 1
                continue
            
            
            if is_word_guessed(word, letters_guessed):
                print("Congratulations, you won!")
                print(f"Your total score for this game is {guess * 2}")
                print("-------------") 
                break
        
        else:
            print("-------------") 
            print(f'Sorry, you ran out of guesses. The word was: {word}')
                
            
            
            
    except Exception as e:
        print(f"Invalid Logic!!, {e}")                
            
            
            
                
                
                
                
                         
                
    
    
    
    # try:
    #     while guess > 0:
    #         print(f"\nYou have {guess} guess left. ")
    #         print(f"Avilable Letters:{get_remaining_letters(letter_guessed)}")
    #         letter_guessed = input("Please guess a letter: ").lower()
    #         while len(letter_guessed) > 1 or not letter_guessed.isalpha() :
    #             guess -= 1
    #             print(f"You have only {guess} guess left")
                
        
    #             if guess == 0:
    #                 print(f"Sorry, you ran out of guesses. The word was: {word}")
    #                 break
                
    #             letter_guessed = input("Please Enter only one letter, guess a letter: ").lower() 
            

    # except Exception as e:
    #         print(f"Invalid Conditoning!!,{e}")
            
            
            
    #         word_guessed = is_word_guessed(word, letter_guessed)
    #         while word_guessed:
    #             remaning_ascii = get_remaining_letters(letter_guessed)
    #             print(f"Avilable Letters: {remaning_ascii}")
            
            
            
            
            
            
            
            
            
            
    

                
                   
               
            
                
    
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
# 
if __name__ == "__main__":
    
   
    # result = load_words()
    # print(result)
    # letter_guessed = ['m','a','l','l','u','a']
    # letterss = get_remaining_letters(letter_guessed)
    # print(letterss)
    
    # guessed_word = is_word_guessed('malla',letter_guessed)
    # print(guessed_word)
    
    # get_guessed = get_guessed_word('majla', letter_guessed)
    # print(get_guessed)
    # Uncomment the line below once you have finished testing.
    
    wordlist = load_words()
    word = choose_random_word(wordlist)
    

    # Uncomment the line below once you have implemented the hangman function.
    hangman(word)
    
    pass