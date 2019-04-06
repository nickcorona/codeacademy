# Write your every_other_letter function here:
def every_other_letter(word):
    letters_lst = []
    length_word = len(word)
    
    # appends every other letter in word to letters_lst
    for i in range(0, length_word, 2):
        letters_lst.append(word[i])

    every_other_letter = ''.join(letters_lst)
    return every_other_letter
        
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 