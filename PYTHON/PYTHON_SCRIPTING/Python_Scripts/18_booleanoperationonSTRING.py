# TO DISPLAY DIFFERENT STRING OPERATIONS
my_str = "Hello World"
print(dir(my_str))
print('\n')



# TRYING OUT DIFFERENT STRING OPERATIONS (startswith('x'), endswith(''), islower(), isupper(), istitle(), isspace(), )
my_str1 = "Python"
print(''''Python' is the String''')
print('Checking if the string starts with p')
print(my_str1.startswith('p'))
print('\n')

print('''The string is 'Python' ''')
print('Checking if the string starts with P')
print(my_str1.startswith('P'))
print('\n')

print('''The string is 'Python' ''')
print('Checking if the starts with Pyth')
print(my_str1.startswith('Pyth'))
print('\n')

print('''The string is 'Python' ''')
print('Checking if the string ends with hon')
print(my_str1.endswith('hon'))
print('\n')

print('''The string is 'Python' ''')
print('Checking if the string is lowercase')
print(my_str1.islower())
print('\n')

print('''The string is 'Python' ''')
print('Checking if the string is UPPERCASE')
print(my_str1.isupper())
print('\n')


my_str2 = 'Python Tutorials'
my_str3 = 'Python tutorials'

print(''' The string is 'Python Tutorials' ''')
print('Checking if the string is a Title')
print(my_str2.istitle())
print('\n')

print('''The string is 'Python tutorials' ''')
print('Checking if the string is a Title')
print(my_str3.istitle())
print('\n')

print('''The string is 'Python Tutorials' ''')
print('Checking if there is any space in the given string')
print(my_str2.isspace())
print('\n')

print('''The string is 'Python' ''')
print('Checking if there is any space in the given string')
print(my_str1.isspace())
print('\n')

my_str4 = 'Python'
print('''The string is 'Pyth0n' ''')
print('Checking if the string consists only of Alphabets')
print(my_str4.isalpha())
print('\n')

#my_str5 = 7904134549
#print('''The string is '7904134549' ''')
#print('Checking if the string is numeric')
#print(my_str5.isnumeric())
#print('\n')