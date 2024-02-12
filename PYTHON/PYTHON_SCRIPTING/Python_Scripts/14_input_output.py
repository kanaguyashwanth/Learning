#addition

'''
#Example 1:
a=5
b=8
result=a+b
print(f"The addition of {a} and {b} is: {result}")
OUTPUT: The addtion of 5 and 8 is: 13
'''

'''
Here, the input will take the values as a string
Example: a=input("Enter a value: ")
         print(f"The value of a is: {a} and the type of a is: {type(a)}"
         #OUTPUT: The value of a is 5 and the type of a is: <class 'str'>
'''

'''
#Example 2:
a=input("Enter a value: ")
b=input("Enter b value: ")
#result=a+b
print(f"The value of a is: {a} and the type of a is: {type(a)}")
#OUTPUT: The value of a is: 7 and the type of a is: <class 'str'>
'''

'''
#Example 3: Reading the input as a String alone, here, we don't have to specify the input in double quotes.
x=input("Enter your string: ")
print(x)
#OUTPUT: this is a string (whatever you input, appears here)
'''

'''
#Example 4: Reading something, and converting it to an integer
x=int(input("Enter x: "))
print(x, type(x))
'''

'''
#Example 5: Evaluation function - Python identifies what kind of data is entered
#By default, this function, stores it as a string, but when a string like hi is entered, it throws an error
#In order to overcome this error, we have to use double quotations like "hi", if we are trying to input string
x=eval(input("Enter x: "))
print(x, type(x))
#INPUT: "This is me"
#OUTPUT: This is me
'''


#Example 6: Simple Addition Calculator - Accepts any string
a=eval(input("Enter a value: "))
b=eval(input("Enter b value: "))
result=a+b
print(f"The addition of {a} and {b} is: {result}")
print(f"The value of a is: {a} and the type of a is: {type(a)}")

#INPUT: a=2, b=3
#OUTPUT: The addition of 2 and 3 is: 5
#        The value of a is: 2 and the type of a is: <class 'int'>

#INPUT: a=2.3, b=3.2
#OUTPUT: The addtion of 2.3 and 3.2 is: 5.5
#        The value of a is: 2.3 and the type of a is: <class 'float'>

#INPUT: a='2.3', b='3.2'
#OUTPUT: The addition of 2.3 and 3.2 is: 2.33.2
#        The value of a is: 2.3 and the type of a is: <class 'str'>



'''
#Example 7: Simple Addtion Calculator - Accepts only integer
a=int(input("Enter a:"))
b=int(input("Enter b:"))
result=a+b
print(f"The addition of {a} and {b} is: {result}")
print(f"The value of a is: {a} and the type of a is: {type(a)}")
'''
#NOTE: Always try to use python3 as python2 doesn't support float in eval function


