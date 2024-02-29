#COUNT - Used to count how many times a particular character appears in a String
print("The String is:")
x = "Python is easy and it is popular language"
print(x)
print('\n')

print("Number of is:")
print(x.count('is'))
print('\n')

print("Number of a:")
print(x.count('a'))
print('\n')

print("Number of easy:")
print(x.count('easy'))
print('\n')

#INDEX - The Index number of a particualr character, INDEX is looked from left to right, and gives the first index value
print("Printing the Index number of a character-P")
print(x.index('P'))

print('Looking for index from particular index value  (After Index-1)')
print(x.index('p', 1)) #Looking for the next index value of p

print("Printing the index from a particular index value (After Index-26)")
print(x.index('p', 26)) #Looking for the next index value of p

#print("Trying to find the index value past the presence of that character, leads to error")
#print(x.index('p', 28))

#Note - If you are trying to look for Index past the presesnce of that character, then it will throw error


#FIND - Finding the Index of a particular character
print("Printing the Index number of a character")
print(x.find('p'))

print('Looking for index from particular index value  (After Index-1)')
print(x.find('p', 1)) #Looking for the next index value of p

print("Printing the index from a particular index value (After Index-26)")
print(x.find('p', 26)) #Looking for the next index value of p

print("Trying to find the index value past the presence of that character, it displays -1, which means that character is not there")
print(x.find('p', 28))


#How FIND is useful? - It will be useful to take decision
java_version = "java version 1.6"
print("Trying to find if java is present, and if it there")
print(java_version.find('java'))

java_version = "error while finding"
print("Try to find if java is there, but it is not there")
print(java_version.find('java'))
