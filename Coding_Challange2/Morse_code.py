# A Morse code encoder/decoder


import os


MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)

def print_intro():
    print("Welcome to Raj'Morse\n")
    print("This program encodes and decodes morse code.\n")
    


def get_input():
    
    while True:
        inputt = input("Would you like to endode(e) or decode(d): ").lower()
        
        if not inputt:
            break
        elif inputt == 'd' or inputt == 'e':
            return inputt
            
        else:
            print("Invalid Mode. Please enter 'e' to encode and 'd' to decode: " )


def encode(message):
    encode_message = []
    morse_code_dict = {}
    for code,word in MORSE_CODE:
        morse_code_dict[word] = code
        
    for char in message:
        if char.upper() in morse_code_dict:
            encode_message.append(morse_code_dict[char.upper()])
        else:
            encode_message.append(" ")
            
    return " ".join(encode_message)            
            


def decode(message):
    decode_message = []
    morse_code_dict = {}
    
    
    for code, word in MORSE_CODE:
        morse_code_dict[code] = word
    
    
    if isinstance(message[0],list):
        for morse_code_sublist in message:
            word = ''
            for morse_code in morse_code_sublist:
                if morse_code in morse_code_dict:
                    word += morse_code_dict[morse_code]
                    
                else:
                    if word:
                        decode_message.append(word)
                        word = ''
                   
                        
            if word:
                decode_message.append(word)  
        
        result =  ' '.join(decode_message) 
        write_lines(result)
        return result
                    
                
    else:
        word = ''
        for morse_code in message:
            if morse_code in morse_code_dict:
                word += morse_code_dict[morse_code] 
            
            elif word: 
                    decode_message.append(word)
                    word = ''

            else:
                if morse_code == " ":
                    decode_message.append(" ")
            
        if word:
            decode_message.append(word)        
    return ' '.join(decode_message)        
                
                                    
            
            
    # for morse_code in message:
    #     new_morse_code = morse_code.strip().split()
    #     hash_morse_code += (new_morse_code,)    
        
    #     if hash_morse_code in morse_code_dict:
    #         decode_message.append(morse_code_dict[hash_morse_code])
    #     else:
    #         decode_message.append(" ")
    #     return " ".join(decode_message)            
        
    
    
        # if hash_morse_code in morse_code_dict:
        #     decode_message.append(morse_code_dict[morse_code])
        # else:
        #     decode_message.append(" ")
        # return " ".join(decode_message)
            
        
    #     if morse_code in morse_code_dict:
    #         decode_message.append(morse_code_dict[morse_code])
    #     else:
    #         decode_message.append(" ")
    # return " ".join(decode_message)            
                
    

# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    check_file = check_file_exists(filename)
    new_list = []
    if check_file:
          
        with open(filename,mode) as f:
            for line in f:
                parts = line.strip().split( '/' )
                for part in parts:
                    new_parts = part.split()
                    new_list.append(new_parts)
            result = decode(new_list)
            return result
    
    return ""    
                
    


def write_lines(lines):
    file_path = "morse_output.txt"
    if os.path.exists(file_path):
        with open(file_path, 'a+') as f:
            f.write(lines)
            print(f"Content Written: {lines}")
    else:
        print(f'File exist but is not empty, {file_path}')
                

def check_file_exists(filename): 
    check_file = os.path.isfile(filename)
    if check_file:
        return True
    else:
        return False
      
    pass

def get_file_input():
    file_input = input("Would you like to encode(e) or decode(d): ").lower()
    while file_input not in {'e','d'}:
        file_input = input("Invalid Choice!!, Please enter 'e' to encode and 'd' decode: " )
    
    file_or_console = input("Would You like to read from a file (f) or the console (c)? ").lower()
    
    while file_or_console not in {'c' , 'f'}:
        file_or_console = input("Invalid Input!!, Please enter either (c) for console and (f) to read from file ") 
           
        
    if file_or_console == 'f':
        filename = input("Enter the file name example: morse_code.txt: ").strip()
        mode = 'r'
        result = process_lines(filename,mode)
        return result
        
    if file_or_console == 'c':
        return file_input
    
        
        
        
            
    

"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.

Hints:
    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment specification for code examples.
"""
def main():
    
    
    
    
    
    while True:
        print_intro()
        user_choice = get_file_input()
        if user_choice == 'e':
            message = input("What would you like to encode: ")
            result = encode(message) 
        elif user_choice=='d':
            Morse__code  = input("what message would you like to decode: ")
            message = Morse__code.split(" ")
            result = decode(message)
    
        print(result)
        
        
        again = input("Would you like to encode/decode another message? (y/n): ").lower()
        if again != 'y':
            print('Goodbye!!')
            break
            


# Program execution begins here
if __name__ == '__main__':
    main()
