#This module hides the password which is being typed on the text field

import getpass
db_pass = getpass.getpass(prompt='Enter your db pass: ')
print(f"The entered password is: {db_pass}")