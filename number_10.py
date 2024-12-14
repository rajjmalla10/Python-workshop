def num_vowel_consonants(letters):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonants_count = 0
    
    for char in letters:
        if char.isalpha():
            if char in vowels:
                vowel_count +=1
            else:
                consonants_count += 1     
               
    
    return vowel_count, consonants_count


letter = input("Enter a sentence, about yourself: ")
sentence = letter.lower()
sentence = ''.join(char for char in sentence if char.isalpha() or char.isspace()) 
vowel_count, consonant_count = num_vowel_consonants(sentence)
print(f"The following sentence Vowel count is {vowel_count} and Consonant count is {consonant_count}")