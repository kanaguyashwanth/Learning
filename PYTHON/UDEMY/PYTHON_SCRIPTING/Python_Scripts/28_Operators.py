#ARITHMETIC OPERATORS
''' Addition (+), 
    Subtraction (-), 
    Multiplication (*), 
    Division (/), 
    Modulo (%), 
    Floor Division (//)
    Exponential (**) '''


#ASSIGNMENT OPERATORS
'''Assignment Operator works in such a way that it ignores the left side first,
computes whatever is present on the right side of the assignment operator (=), then assigns it to the left side,
'''

''' ASSIGNMENT OPERATORS:
    Operator    Example     Same as
    =           a=b         a=b     
    +=          a+=b        a=a+b   
    -=          a-=b        a=a-b   
    *=          a*=b        a=a*b   
    /=          a/=b        a=a/b   
    %=          a%=b        a=a%b   '''

a=2
b=3

#ADDTION 
# [a+=b ---> a=a+b]
print('add')
add = a+b
print(add)
print('\n')

#SUBTRACTION 
# [a-=b ---> a=a-b]
print('subtract')
subtract = (a-b)
print(subtract)
print('\n')

#MULTIPLICATION   ---> By default (Python3), Result is in FLOAT
# [a*=b ---> a=a*b]
print('multiply')
multiply = (a*b)
print(multiply)
print('\n')

#DIVISION         ---> By default (Python3), Result is in FLOAT
# [a/=b ---> a=a/b]
print('divide')
divide = a/b
print(divide)
print('\n')

#EXPONENTIAL
print('exponential')
exponent = a**b
print(exponent)
print('\n')

#MODULO
# [a%=b ---> a=a%b]
print('modulo')
modulo = a%b
print(modulo)
print('\n')

#FLOOR DIVISION  ---> Divides and then floors the value (Rounding down)
print('floor div - b//a')
print('Example 1: [3//2]')
floor_div = b//a
print(floor_div)
print('Example 2:[-9//5]')  #Here, it rounds it down to the lowest value
floor_div = -9//5
print(floor_div)
print('\n')


