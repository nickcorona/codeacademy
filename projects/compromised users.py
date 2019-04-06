import csv
import json

compromised_users = []
with open('projects/passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for line in password_csv:
        password_row = line
        compromised_users.append(password_row['Username'])

print(compromised_users)

with open('compromised_users', 'w') as compromised_user_file:
    compromised_user_csv = csv.writer(compromised_user_file)
    for user in compromised_users:
        compromised_user_csv.writerow(user)


with open('projects/boss_message.json', 'w') as boss_message:
    boss_message_dict = {}
    boss_message_dict['recipient'] = 'The Boss'
    boss_message_dict['message'] = 'Mission Success'
    json.dump(boss_message_dict, boss_message)

with open('projects/new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = r"""
     _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
    """
    new_passwords_obj.write(slash_null_sig)