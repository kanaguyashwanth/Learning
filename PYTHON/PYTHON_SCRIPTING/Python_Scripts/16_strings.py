#EXAMPLE 1:
print("EXAMPLE 1")
my_name = 'Yashwanth'
my_new_name = "Python Scripter"
my_info = """ I started my career as a Technical Solutions Consultant """
print(f'My name is: {my_name}\nMy new name is: {my_new_name}\nMy info is: {my_info}')
print("\n")

#EXAMPLE 2: Whatever is provided in the triple quotes, the same format will be preserved.
print("EXAMPLE 2:")
my_name = 'Yashwanth'
my_new_name = 'Python Scripter'
my_info = """
I started my career as a Technical Solution Consultant
and moved to nowhere
"""
print(f'My name is: {my_name}\nMy new name is: {my_new_name}\nMy info is: {my_info}')
print("\n")

#EXAMPLE 3: Proving that space is also a string.
print("EXAMPLE 3:")
my_str = ""
my_new_str = " "
print(f'my_str has ""(no space): {bool(my_str)}\nmy_new_str has " "(has space): {bool(my_new_str)}')
print("\n")

#EXAMPLE 4: Accessing a character from a string. (Using positive index values)
print("EXAMPLE 4:")
my_string = "this is positive indexing"
print(my_string[0]) #This displays the first character of a string
print(my_string[1])
print(my_string[2])
print(my_string[3])
print("\n")

#EXAMPLE 5: Accessing string from the end. (Using -1 in index to access the last character of a string) (Using negative index values)
print("EXAMPLE 5:")
my_string2 = "this is negative indexing"
print(my_string2[-1]) #This displays the last character of a string
print(my_string2[-2])
print(my_string2[-3])
print(my_string2[-4])
print(my_string2[-5])
print(my_string2[-6])
print(my_string2[-7])
print(my_string2[-8])
print("\n")

#EXAMPLE 6: Printing the string from a range
print("EXAMPLE 6:")
my_string3 = "Python is cool"
str_0_4 = my_string3[0:5] #RANGE is 5
str_1_4 = my_string3[1:5] #RANGE is 4
print(str_0_4)
print(str_1_4)
print("\n")


#EXAMPLE 7: Printing the string from a given index till the end of the string
print("EXAMPLE 7:")
my_string4 = "Python scripting is ezpz"
str_4_end = my_string4[4:]
print(str_4_end)
print("\n")


#EXAMPLE 8: Printing the string from starting till the given index
print("EXAMPLE 8:")
my_string5 = "Python scripting is so big"
str_start_9 = my_string5[:9]
print(str_start_9)
print("\n")


#EXAMPLE 9: Finding the length of a string
print("EXAMPLE 9:")
my_string6 = "This is a string"
str_len = len(my_string6)
print(f'The string is: {my_string6}')
print(f"The length of the string is: {str_len}")
print("\n")


#EXAMPLE 10: Experimenting with negative indexing
print("EXAMPLE 10:")
my_string7 = "Python tutorials"
print(f'The string is: {my_string7}')
print(f'String starts with: {my_string7[0]}')
print(f'String ends with: {my_string7[-1]}')
print(f'string[-16:-5]: {my_string7[-16:-5]}')     #Starts from -16, prints till (-5-1)=-6
print(f'string[-5:-16]: {my_string7[-5:-15]}')     #Not Possible - Why?
print("\n")


#EXAMPLE 11: Concatenating/Adding two strings
print("EXAMPLE 11:")
my_string_a = "Python"
my_string_b = "Tutorial"
my_string_space = " "
my_string_d = my_string_a + my_string_space + my_string_b
print(my_string_d)
#OR you can do the below thing
my_string_e = my_string_a + " " + my_string_b
print(my_string_e)
print("\n")


#EXAMPLE 12: Case Conversion Operations
print("EXAMPLE 12:")
my_string_8 = "Python Scripting"
print(my_string_8.lower())
print(my_string_8.upper())
print(my_string_8)
print("\n")


#EXAMPLE 13: Case conversion, but storing them in a variable
print("EXAMPLE 13:")
my_string_9 = "Scripting is not a language"
my_string_lower = my_string_9.lower()
my_string_upper = my_string_9.upper()
print(my_string_9)
print(my_string_lower)
print(my_string_upper)
print("\n")
