vowel = {'a','e','i','o',
'u'}

def count_vowel(vowel):
    count = 0
    word = input("enter any english word: ").lower()
    for char in word:
        if char in vowel:
            count += 1    
    if count == 0:
        print('word doesnt contain any vowel')    
    else:
        return count    

result = count_vowel(vowel)
print(result)