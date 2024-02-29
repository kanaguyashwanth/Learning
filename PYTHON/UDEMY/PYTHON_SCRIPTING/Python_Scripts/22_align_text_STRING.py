#Run this script in cmd

import os
t_w = get_terminal_size().columns

given_str = input("Enter string: ")
print(given_str.center(t_w).title())
print(given_str.ljust(t_w).title())
print(given_str.rjust(t_w).title())

