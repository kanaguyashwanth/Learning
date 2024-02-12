# STRIP - Removes the spaces or words on either sides of the string
my_string1 = "   Python "
my_string2 = "Python"
print("String1: ")
print(my_string1)
print('\n')

print("Printing the string with spaces removed using strip")
print(my_string1.strip())
print('\n')

print("Removing the first letter from the string")
print(my_string2.strip('P'))
print('\n')




my_string3 = "Python scripting is ezpz"
print("String2: ")
print(my_string3)

print('Printing the string with ezpz(word) removed using rstrip or lstrip')
print(my_string3.rstrip('ezpz'))
print('\n')

print("Printing the string with Python removed, usig lstrip")
print(my_string3.lstrip('Python'))
print('\n')


my_string4 = "pythonyy"
print("Using combinations of strip functions like strip(p).lstrip(y), THIS WILL ONLY REMOVE THE y PRESENT ON LHS of STRING and ALSO REMOVES p")
print("The string is: "); print(my_string4)
print('After stripping: ')
print(my_string4.strip('p').rstrip('y'))
print('\n')





# SPLIT OPERATION: (String gets Split into a LIST wherever there are SPACES)
print("SPLIT OPERATIONS: (Splits it into a LIST)")
my_string5 = "Python is Easy"
print(f"The string is: {my_string5}");
print(my_string5.split())

# PERFORMING A STRIP OPERATION AFTER SPLIT
print("After SPLIT, we are STRIPING")
my_string6 = "Learning is good"
print(f"The string is: {my_string6}")
print(my_string6.split())       #Splitting wherever there is SPACE
print(my_string6.split('is'))   #Splitting wherever there is 'is'