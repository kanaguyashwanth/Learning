# CODING EXERCISE: Sum of Digits
'''
Enter a two digit number: 26 ---> OUTPUT: 8
'''

num = input ("Enter a two digit number: ")
first_digit = int(num[1])
last_digit = int(num[0])
print ("Sum of digits: " + str(first_digit + last_digit))
# OR
print (f"Sum of digits: {first_digit + last_digit}")        # f-string

print(type(num))
# print(type(n_2_str))