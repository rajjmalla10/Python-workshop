def word_intersection():
    first_word = set(input("enter any word: "))
    second_word = set(input("enter second word: "))
    common_letter = first_word.intersection(second_word)
    return common_letter
result = word_intersection()
print(result)            
        
    