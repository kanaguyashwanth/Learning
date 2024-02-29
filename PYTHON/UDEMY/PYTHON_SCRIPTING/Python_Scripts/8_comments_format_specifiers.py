#This is a single-line comment
#For this we use hash (#)
#This is a simple arithmetic calculator
#Author: Yashwanth K
#Date: October-2022
#Version: v2.2

'''
This is a multiple-line comment
For this we use triple quotes (')
This is a simple arithmetic calculator
Author: Yashwanth K
Date: October-2022
Version: v2.2

'''

a=4
b=5
result=a+b

#Printing formatted strings
print(f"The addition of {a} and {b} is: {result}")
print('\n')


#Few other examples of formatted strings
print('Example: 1')
name = 'Yashwanth'
print(f'He said his name is {name}')     #OUTPUT: He said his name is Yashwanth
print('\n')

# Printable representation of strings
print('Example 2:')
name = 'Yashwanth'
print(f'He said his name is {name!r}')   #OUTPUT: He said his name is 'Yashwanth'
print('\n')

print('Example 3:')
name = 'Yashwanth'
print(f'He said his name is {repr(name)}')   #OUTPUT: He said his name is 'Yashwanth'
print('\n')

#Note: repr() is equivalent to !r

#Integer Format Specifier
print('Example 4:')
number = 1024
print(f'{number: #0x}')



#MORE Format Specifiers
'''
 - Nest and format
 - __format__ [Uses calss and definitions]
 - Pretty formatting
 - Zero-padding, float, percentage rounding
'''