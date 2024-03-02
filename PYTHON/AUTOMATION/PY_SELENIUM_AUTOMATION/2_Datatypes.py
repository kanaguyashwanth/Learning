# Printing and its datatypes
a, b, c = 5, 6.4, 'Great'
print(f'a: {a}  {type(a)},\nb: {b}  {type(b)},\nc: {c}  {type(c)}')
print('\n*****************************\n')




# DATATYPES:
'''
1. NUMERIC:
    - int
    - float
    - complex
'''
a=10
b=10.1
c=10+1j
print(f'a: {a}  {type(a)},\nb: {b}  {type(b)},\nc: {c}  {type(c)}')
print('\n*****************************\n')




# 2. STRING [NOTE: We can only concatenate strings and not different datatypes]
a='This is '
b='a string'
print(f'a+b: {a+b}  {type(a+b)}')
print('\n*****************************\n')




# 3. LIST:
values = [1, 2, 'rahul', 4]
print(f'Whole string: {values}')
print(f'First Index: {values[0]}')
print(f'Last Index: {values[-1]}')
print(f'Some Index: {values[2]}')

# Slicing the list
print(f'Slicing Index[1:3]: {values[1:3]}')

# Inserting Item between the list
values.insert(3,"me")
print(values)

# Adding Item to end of list
values.append('end')
print(values)

# Updating List
values[2] = 'rooooohooool'