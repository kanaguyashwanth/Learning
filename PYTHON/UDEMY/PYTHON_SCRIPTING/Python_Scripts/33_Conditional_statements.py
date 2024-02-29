#SYNTAX
'''
if expression:
    statement1
    statement2
'''

#EXAMPLE 1: Text Align
import os
t_w = os.get_terminal_size().columns

given_str = input("Enter your strings: ")
print(given_str)
user_cnf = input("Do you want to align text: Yes(Y) or No(N)?: ") #user_cnf - User confirm variable
if user_cnf == "Yes" or "yes" or "Y" or "y":
    print(given_str.center(t_w).title())
    print(given_str.ljust(t_w).title())
    print(given_str.rjust(t_w).title())


#EXAMPLE 2: Convert given string into lowercase
'''
user_str = input("Enter your string: ")
user_cnf = input("Do you want to convert your string into lowercase: YES(Y) or NO(N))

if user_cnf = "yes"
    print(user_str.lower())
'''

#EXAMPLE 3: Check if even nos. are available
'''
my_even_nos = [0, 2, 4, 6, 8, 10]
user_num = eval(input("Enter your number: "))

if user_num in my_even_nos:
    print("Your given no. is Even")
'''

#EXAMPLE 4: Find greater number
'''
a = eval(input("Enter your firts mnumber"))
b = eval(input("Enter your second number"))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{b} is greater than {a}')
elif a==b:
    print(f'{a} and {b} are equal')
'''

#EXAMPLE 6: Print any nyumber between 1-10
'''
num = eval(input("Enter any number between 1-10 range: "))
num_word = [1:'one', 2:'two', 3:'three', 4:'four', 5: 'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten']

if num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(num_word.get(num))
else:
    print("Your number is out of range, please select 1-10 range")
'''