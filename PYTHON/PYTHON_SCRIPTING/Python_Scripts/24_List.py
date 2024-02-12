#Note - LISTS are MUTABLE, we can change the part of LIST
#       STRINGS are IMMUTABLE, cannot change the part of STRING

'''
Go to cmd
my_list=[3, 4, 5]
dir(my_list)

OUTPUT: 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
Here, anything that is displayed without the underscores are the String Operations, like the above ones.
'''

#examples_of_string_operations
#EXAMPLE_1: INDEX - To find the index of that particular element
print('Using different string operations: ')
my_list = [3, 5, 2, 7, 3, 8, 9, 5]
print(my_list.index(5)) #If value is not UNIQUE, then print(my_list.index(5, 1))
print('\n')

#EXAMPLE_2: COUNT - To count the number of times a particular element occurrs in the list
print('Using count operation to count the particualr element: ')
print(my_list.count(5))
print('\n')

#EXAMPLE_3: CLEAR - To clear the list
print('Using clear operation to clear the list: ')
print('Before clearing: ')
print(my_list)
print('After clearing: ')
my_list.clear()
print(my_list)  #Since, List is MUTABLE, we can directly use the operation, than using clear operation inside the print statement like print(my_list.clear())
print('\n')

#EXAMPLE_4: COPY - Copying the data from one list to another
my_new_list = my_list         #ASSIGNING -----> the variable my_new_list is pointing to the memory address location of my_list
my_one_more = my_list.copy()  #COPYING   -----> the variable my_one_more is a new different address memory location where the contents of my_list are being copied to this list
print('Memory locations of my_new_list and my_list')
print(id(my_new_list), id(my_list))
print('Memory location of my_one_more')
print(id(my_one_more))
print('\n')

#EXAMPLE_5: APPEND - Add element at end of list, if there is another list which u tried to append, then that list will be inside another list
#           INSERT - Add element inbetween list
#           EXTEND - Add element at end of list, if there is another list which u tried to extend, then all the contents of this list are sent to the other list
print('Printing a list before appending: ')
my_list3 = [3, 5, 2, 7, 3, 8, 9]
print(my_list3)
my_list3.append(100)  #The list would now be, my_list3 = [3, 5, ,2, 7, 3, 8, 9]
print('Printing the list after appending: ')
print(my_list3)
print('\n')

print("Using INSERT operation to insert data inbetween a list: ")
print('Printing list before inserting: ')
print(my_list3)
my_list3.insert(1, 200)   #Note ---> my_lsit3.insert(index, value)
print("Printing list after inserting: ")
print(my_list3)
print('\n')

print("Difference between APPEND and EXTEND: ")
my_new_list1 = [5, 6]
my_new_list2 = [3, 5, 2, 7, 3, 8, 9, 5]
my_new_list3 = [3, 5, 2, 7, 3, 8, 9, 5]
print("List1: ")
print(my_new_list1)
print("List2:")
print(my_new_list2)
print("Performing APPEND operation: ")
my_new_list2.append(my_new_list1)
print(my_new_list2)
print('Performing EXTEND operation: ')
my_new_list3.extend(my_new_list1)
print(my_new_list3)
print('\n')

#EXAMPLE_6: REMOVE - Removes the value directly
#           POP    - By Default, POP removes the last data, Removes based on Index position given, if Index position is given, then it will remove the data on that position
#                  - When POP is used, it will modify the List. When used inside print statement like print(my_list.pop()) -----> This will display the data that is being removed
#           Note:  - POP - uses index value to remove that particualr data, if not provided then it will remove the last data in the List
#                  - REMOVE - When a particular value present in the list is mentioned in the remove operation, it will remove that particular data

#EXAMPLE_7: REVERSE - Just reverses the whole list




#empty list
my_list1 = []
print('This is an empty list')
print(my_list1)
print('\n')



#Non-empty list
my_list2 = [2, 3, 4, 'python', 5.6]
print('This is a non-empty list')
print(my_list2)
print('\n')



#boolean of empty list is FALSE
print('Boolean of an EMPTY list is: ')
print(bool(my_list1))
print('\n')



#boolean of non-empty list is TRUE
print('Boolean of a non-empty list is: ')
print(bool(my_list2))
print('\n')



#INDEXING - STRING vs. LIST
'''
STRING: [Variable]
   "h e l l o"
    | | | | |
    0 1 2 3 4   OR
   -5-4-3-2-1   last index -1

LIST: [Datastructure]
   [3, 4, 5, 'python', 5.6]
    |  |  |     |       |
    0  1  2     3       4    OR
   -5 -4 -3    -2      -1    last index -1

'''


#EXAMPLES_FOR_LISTS - my_list2 = [2, 3, 4, 'python', 5.6]
print('Printing my_list2:')
print(my_list2)
print('\n')

print("Accessing the list using first index")
print(my_list2[0])
print('\n')

print('Accessing the list using forth index')
print(my_list2 [3])
print('\n')



#ACCESSING_THE_CHARACTER_IN_EACH_LIST
print("Accessing the forth element's second index element")
print(my_list2 [3][1])  #Here, my_list[3] is "python" and my_list2[3][1] is "y"
print('\n')



#ACCESSING_THE_ENTIRE_LIST
'''
print(my_list2)
print(my_list2[:])
print(my_list2[0:])
All the above print statements will give the same result and will print from start till the end of the list
'''
print("Accessing the entire list: ")
print(my_list2[:])
print('\n')



#ACCESSING_FIRST_INDEX_TO_LAST -----> my_list2 = [2, 3, 4, "python", 5.6], OUTPUT: [3, 4, "python", 5.6]
print("Accessing from first index of list to last")
print(my_list2[1:])
print('\n')



#ACCESSING_FIRST_TO_NEXT_3_INDEX_VALUES   ----->    4 - 1 = 3 [ Range ]
print('Accessing from the first index to 3 more values')
print(my_list2[1:4])
print('\n')



#MODIFYING_THE_ELEMENTS_IN_THE_LIST
print("Modifying the elements in the list: ")
print("The list before: ")
print(my_list2)
print('\n')
my_list2[1] = 9999999
print("The list after: ")
print(my_list2)
print('\n')
