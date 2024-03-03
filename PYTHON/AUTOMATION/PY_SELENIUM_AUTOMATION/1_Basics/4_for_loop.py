# EXAMPLE 1: (Iterating every element on the list)

a = [4, 8, 2, 13]
for x in a:
    print(x+1)
print('\n*****************************\n')




# EXAMPLE 2: (Sum of first 5 natural numbers)

'''
1 + 2 + 3 + 4 + 5 = 15
'''

sum = 0
n = 0
for i in range(1,6):
    sum += i
print(sum)
print('\n*****************************\n')




# EXAMPLE 3: (for loop with step - Jumping index)
for n in range(1,11,2):
    print(n)
print('\n*****************************\n')




# EXAMPLE 4: (without starting point value, by default, it takes starting point as 0 if not specified.)
for k in range(10):
    print(k)
print('\n*****************************\n')




