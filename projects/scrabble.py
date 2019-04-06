letters = ["A", "B", "C", "D", "E", "F", "G",
 "H", "I", "J", "K", "L", "M", "N", "O", "P",
 "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_to_points = {letter:point for letter, point in zip(letters, points)}

letters_to_points[' '] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points[letter]
  return point_total

brownie_points = score_word('BROWNIE')
print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'],
                  'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
                  'Lexi': ['ERASER', 'BELLY', 'HUSKY'],
                  'ConProf': ['ERASER', 'BELLY', 'HUSKY'],
                  'Reader': ['ZAP', 'COMA', 'PERIOD']}
                             
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
                       

# play_word() — a function that would take in a player and a word,
#  and add that word to the list of words they’ve played
def play_word(player, word):
    player_to_words[player].append(word)

play_word('player1', 'JELLY')
print(player_to_words['player1'])

# update_point_totals() — turn your nested loops 
# into a function that you can call any time a word is played
def update_point_totals():
    player_to_points = {}
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points

update_point_totals()

# make your letter_to_points dictionary able to handle lowercase inputs as well
letters_to_points.update({letter.lower():point for letter, point in zip(letters, points)})
print(letters_to_points)
