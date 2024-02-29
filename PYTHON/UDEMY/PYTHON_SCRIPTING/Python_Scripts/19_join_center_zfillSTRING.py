# JOIN
# If we want to turn "Python" ---> "P y t h o n", then use JOIN
print('Adding space inbetween each character using JOIN')
a = 'Python'
b = ' '.join(a)
print(b)
print('\n')

print('Adding a tabspace between each character using JOIN')
b = '\t'.join(a)
print(b)
print('\n')

# To print it as P*y*t*h*o*n
print('Adding * between each character of a string using JOIN')
b = '*'.join(a)
print(b)
print('\n')

print('Printing each character in new line using JOIN')
b = '\n'.join(a)
print(b)
print('\n')






# CENTER
# CENTER - Centering the string inside a given space
my_string1 = 'Python'
my_string2 = 'Scripting'
my_string3 = 'Operation'
print(my_string1.center(20))
print(my_string2.center(20))
print(my_string3.center(20))
print('\n')

# Using Format print(f"{} \n {} \n {}")
print(f"{my_string1.center(20)}\n{my_string2.center(20)}\n{my_string3.center(20)}")
print('\n')








#ZFILL
# Zero fill - zfill (Padding with zeros)
print(my_string1.zfill(10))
print(my_string3.zfill(12))