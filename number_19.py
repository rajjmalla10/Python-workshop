def word_difference():
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    first_word = set(input("enter any word: ").lower())
    second_word = set(input("enter second word: ").lower())
    difference = first_word.union(second_word)
    result = alphabet - difference
    return result

a = word_difference()
print(a)

    