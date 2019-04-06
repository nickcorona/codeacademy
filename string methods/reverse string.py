# Write your reverse_string function here:
def reverse_string(word):
    reversed_word_lst = reversed(word)
    reversed_word = ''.join(reversed_word_lst)
    return reversed_word

    
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print