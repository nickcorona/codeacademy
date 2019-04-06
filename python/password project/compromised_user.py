import csv

compromised_users = []
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    password_row = line
    compromised_users.append(password_row['Username'])

with open('compromised_users', 'w') as compromised_user_file:   
    compromised_user_csv = csv.writer(compromised_user_file)
    for user in compromised_users:
        compromised_user_csv.writerow(user)
