



# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import os
import random
import string
import sys


class Player_info:
    
    def __init__(self,name,score):
        self.name = name 
        self.score = score
        pass


from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt"
file_name = "words.txt"

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

 
 
def get_score(player_info):
    
    player_name = player_info
    
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for index,line in enumerate(f,start=1):
                if index <= 2:
                    continue
               
            
                parts = line.strip().split()
        
                if len(parts) == 3:
                    sn, name, score = parts
                    if name == player_name:
                        print(f"SN:{sn} name: {name} score: {score}")
                        break
                    
    else:
        print('No match found')    



def save_score(player_name,score):
    
    new_lines = []
    
    file_name = 'scores.txt'
    heading = f"{'SN':<10} {'Name':<10} {'Score':<10}\n{'-'*35}"
    new_lines = []
    
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
            
            #for first two line skipping header
            for line in lines[2:]:
                parts = line.strip().split()
                
                if len(parts) == 3:
                    sn,name,existing_score = parts
                    
                    if name == player_name:
                        
                        existing_score = max(int(existing_score),score) 
                        new_lines.append(f'{sn:<10} {name:<10} {existing_score:<10}')
                        found = True
                    else:
                          
                        
                    
    

    
     
    
    # with open(file_name, 'r') as f:
    #     line = f.read.lines()
        
    # file_empty = len(line) == 0
    
    # with open(file_name,'a') as file:
        
    #     if file_empty:
    #         f.write(f"{headings[0]:<10} {headings[1]:<10} {headings[2]:<10}")
    #         f.write(f"{'-'*30}")
    
    # for index, _ in enumerate(open(file_name)):
    #     if index >= 1:
    #         f.write(f"{index+1} {name} {score}")
             
              
 
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
    try:
        while True:
            
            try:
                view_quit = input("Do you want to Play (p) view the leaderboard (l) or quit (q): ").lower()
                while view_quit not in {'p','l','q'}:
                    view_quit = input("invalid Input!!, Please enter to Play (p) view the leaderboard (l) or quit (q): ").lower()
                    
                if view_quit == 'l':
                    try:
                        player_name = input("Enter the name of the player you want to get information about: ")
                        get_score(player_name)
                    except Exception:
                        print("Enter a valid name.")    
                    pass
    
                elif view_quit == 'p':
                    name = input("What is your name: ").strip().title()
                    break
                
                elif view_quit == 'q':
                    print("Thank you for playing! Goodbye!")
                    sys.exit(0)
            except Exception as e:
                print("Error While loading the menu!: {e}. Please try again")     
    except KeyboardInterrupt:
        print("\nProgram interuptted. Existing gracefully")
        
    except Exception as e:
        print("Ab unexpected error occured. Please find customer support")
       
        
                        
        
    print(f"I am thinking of a word that is {len(word)} letters long")
    print("-------------")
    # TODO: Fill in your code here
    letter_guessed = ''
    
    
            
    
    
    try: 
        while guess > 0:
            print(f"\nYou have {guess} guesses left. ")
            print(f"Avilable letters:{get_remaining_letters(letter_guessed)}")
            letter_guessed = input("Please guess a letter: ").lower()
            
            
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
                print(f"Oops! That letter is not in my word: {get_guessed_word(word, letters_guessed)}")
                print("-------------")
            
            
            if is_word_guessed(word, letters_guessed):
                print("Congratulations, you won!")
                score = guess * len(set(word))
                
                print(f"Your total score for this game is {score}")
                save_score(name,score)
                print("-------------") 
                break
        
        if guess <= 0:
            
            score = guess * 2
            print("-------------") 
            print(f'Sorry, you ran out of guesses. The word was: {word}')
            save_score(name,score)    
            
            
            
    except Exception as e:
        print(f"Invalid Logic!!, {e}")                
            
            
            

    
    
    try:
        while guess > 0:
            print(f"\nYou have {guess} guess left. ")
            print(f"Avilable Letters:{get_remaining_letters(letter_guessed)}")
            letter_guessed = input("Please guess a letter: ").lower()
            while len(letter_guessed) > 1 or not letter_guessed.isalpha() :
                guess -= 1
                print(f"You have only {guess} guess left")
                
        
                if guess == 0:
                    print(f"Sorry, you ran out of guesses. The word was: {word}")
                    break
                
                letter_guessed = input("Please Enter only one letter, guess a letter: ").lower() 
            

    except Exception as e:
            print(f"Invalid Conditoning!!,{e}")
            
            
            
            word_guessed = is_word_guessed(word, letter_guessed)
            while word_guessed:
                remaning_ascii = get_remaining_letters(letter_guessed)
                print(f"Avilable Letters: {remaning_ascii}")
            

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