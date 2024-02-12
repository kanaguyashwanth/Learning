#Define a Tuple
print('Defining and printing a tuple')
my_empty = ()
my_tuple = (3,4,5)
print(my_empty)
print(my_tuple)
print('\n')

#Converting empty tuple to Boolean
print(bool(my_empty))
print('\n')

#Converting non-empty typle to Boolean
print(bool(my_tuple))
print('\n')

#Tuple can contain a List inside
print("Tuple with a List inside:")
my_tuple1 = (3,4,[1,2,3],5,6)
print(my_tuple1)
print('\n')

'''
Note: INDEXING
my_tuple1 = (3 ,4 , [1, 2, 3], 5, 6)
             |  |       |      |  | 
             0  1       2      3  4   
'''

#Printing tuple based on Index value
print("Printing Tuple using Index value")
print(my_tuple1[0])
print(my_tuple1[1])
print(my_tuple1[2])
print(my_tuple1[3])
print(my_tuple1[4])
print("\n")

#Printing each element of the List inside Tuple
print("Printing each element in the List inside a Tuple")
print(my_tuple1[2][0])
print(my_tuple1[2][1])
print(my_tuple1[2][2])
print('\n')

'''
TUPLES ARE IMMUTABLE - But can Modify the entire Tuple
Note: Tuple Object does not support Item assignment
-Once the values are defined, we cannot change any value or item inside Tuple.
-Modifying part of Tuple is not possible, but modifying the entire tuple is possible.
-Which means when we try to try to change the element in a particular index, it throws error.
-Go to cmd - x = (4,5)
             dir(x)
-You will find that there are NO much operations for tuple
'''

'''
Note: Length Operation:
    -If it is a List, then it displays length of List
    -If it is Tuple, then it displays length of Tuple
'''

#All the INDEX OPERATIONS performed on a List is same for Tuples as well
#Refer 24_List.py


#Datatype
print("Printing Datatype: ")
x=5  #Integer 
y=5, #Tuple datastructure variable
print(x, type(x))
print(y, type(y))


#Note: Lists - MUTABLE
#      Tuple - IMMUTABLE

