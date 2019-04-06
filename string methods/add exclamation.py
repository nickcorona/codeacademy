# Write your add_exclamation function here:
def add_exclamation(word):
    length_word = len(word)
    if length_word >= 20:
        return word
    else:
        exclaimed_word = word + '!' * (20 - length_word)
        return exclaimed_word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn