# The poetry organization has sent over the bio for Jean Toomer as it currently exists on their site. 
# Notice that there was a mistake with his last name and all instances of Toomer are lacking one o.
# Use .replace() to change all instances of Tomer in the bio to Toomer. Save the updated bio to the string toomer_bio_fixed.
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)