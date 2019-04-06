# They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. 
# They want you to join together all of the lines into a single string that can be used to display the poem again, but this time,
# you’ve noticed that the list contains a ton of unnecessary whitespace that doesn’t appear in the actual poem.
# First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
 '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    stripped_line = line.strip()
    love_maybe_lines_stripped.append(stripped_line)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)