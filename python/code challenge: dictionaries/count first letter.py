# Write your count_first_letter function here:
def count_first_letter(my_dictionary):
    first_letters = set()
    for key in my_dictionary:
        first_letters.update(key[0])
    offsprings = {}
    for first_letter in first_letters:
        count_offspring = 0
        for key, value in my_dictionary.items():
            if key[0] == first_letter:
                count_offspring += len(value)
            else:
                continue
        offsprings[first_letter] = count_offspring
    return offsprings

        
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}