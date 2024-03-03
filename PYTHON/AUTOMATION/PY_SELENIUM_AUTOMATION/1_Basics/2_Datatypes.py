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
print(f'Slicing Index[1:3]: {values[1:3]}') # Slicing the list
values.insert(3,"me")        # Inserting Item between the list
print(values)
values.append('end')                        # Adding Item to end of list
print(values)
values[2] = 'rooooohooool'                  # Updating List
print('\n*****************************\n')




# 4. TUPLES:
a = ('kennedy', 2, 3.14, 3+2j)               # Tuples can also have multiple datatypes
print(a)                                     # Same as List but IMMUTABLE
print(a[3])
print('\n*****************************\n')




# 5. DICTIONARY:
c = {'a': 1, 2: 'b', 'age': 3, 'four': 'nothing'}              # Key-Value Pair
print(c)
print(c['a'])
print(c[2])
print(c['age'])
print(c['four'])
print('\n*****************************\n')




# Creating Dictionaries at runtime and adding data into it

dict = {}   # Create empty dictionary

dict['firstname'] = 'yashwanth'
dict['lastname'] = 'k'
dict['gender'] = 'male'
print(dict)
print('\n*****************************\n')