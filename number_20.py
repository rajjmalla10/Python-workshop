def word_sdifference():
    first_word = set(input("enter any word: ").lower())
    second_word = set(input("enter second word: ").lower())
    s_difference = first_word.symmetric_difference(second_word)
    return s_difference

result = word_sdifference()
print(result)
    