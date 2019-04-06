# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    first_letter1 = word1[0]
    first_letter2 = word2[0]
    spoonered_word1 = first_letter2 + word1[1:]
    spoonered_word2 = first_letter1 + word2[1:]
    spoonered_words = ' '.join([spoonered_word1, spoonered_word2])
    return spoonered_words


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a