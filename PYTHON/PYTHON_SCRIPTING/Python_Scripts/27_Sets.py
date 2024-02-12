#Sets are UNORDERED Collection of Data because it displays in an ascending way
#Duplicates are removed in Sets

#Printing the SET
my_set = {4, 5, 7, 2, 7, 0}
print(my_set)
bool(my_set)
print('\n')

#EMPTY SET
my_set = set({})  #my_set = {} is wrong because it is a dictionary
print(type(my_set))
bool(my_set)
print('\n')

#Converting a list to SET
my_list = [4, 5, 6, 7,5]
print('Printing list: ')
print(my_list)
print('\n')
print('Printing set: ')
print(set(my_list))
print('\n')

#SET OPERATIONS - dir(set) - intersection, isdisjoint, union, issubset, issuperset, pop, remove, update
a = {3, 4, 5, 6}
b = {5, 6, 7, 8, 9}
print('a: ' )
print(a)
print('\n')
print('b: ')
print(b)
print('\n')

print('A union B')
print(a.union(b))
print('\n')

print('A intersection B')
print(a.intersection(b))
print('\n')
