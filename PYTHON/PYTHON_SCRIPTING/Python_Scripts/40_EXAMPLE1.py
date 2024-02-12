'''
Script has to read string and convert it 
into upper, lower, title format
'''

#Note: THis script needs 2 inputs - Strings and User Action


#EXAMPLE1: THIS EXAMPLE NEEDS 2 INPUTS - STRING AND USER_ACTION
usr_str = input("Enter your string: ")
usr_action = input("Enter action: [lower/upper/title] to the string: ")


if (usr_action=="lower"):
    print(usr_str.lower())

elif (usr_action=="upper"):
    print(usr_str.upper())

elif (usr_action=="title"):
    print(usr_str.title())


#Refer 40_EXAMPLE2.py - One input for the above example

