given_str = input("Enter your string: ")
print(given_str)

#By default,, python displays the data on the LEFT side. When you try to print a string, it prints on the left side.
#Now, try to display the string on the CENTER and on the RIGHT side of the dislpay.
#In order to display it on the RIGHT/CENTER, we have to know how many COLUMNS / WIDTH of the line
#WINDOWS - cmd - type 'mode' and it will display the number of columns
#VSCODE - type mode in terminal - column - 117

#cmd - python terminal >>>
'''
import os
os.get_terminal_size()                      #gives columns and lines but if you want only columns, then
os.get_terminal_size().columns              #gives only columns
//t_w = os.get_terminal_size().columns      #terminal width

'''

print(given_str.center(177))
print(given_str.ljust(177))
print(given_str.rjust(177))



