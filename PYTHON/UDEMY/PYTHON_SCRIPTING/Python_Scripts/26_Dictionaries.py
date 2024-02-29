#REPRESENTATION - SYNTAX
print('Dictionary Syntax:')
my_dict1 = {}
print(my_dict1, type(my_dict1))
print(bool(my_dict1))
print("\n")

#DICTIONARY SHOULD BE WRITTEN IN THE FORM OF KEY:VALUE PAIR
#   KEY:VALUE Pair ---> Dictionary
#   If the Key/Value are strings, then it has to be written in quotations
#   In order to access the values, we need the keys

#WAYS OF ACCESSING THE VALUES BY PROVIDING THE KEY
print('Accessing the values of the Dictionary:')
my_dict2 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2}
print(my_dict2)
print(my_dict2['fruit'])      #Throws error when the value is not present
print(my_dict2.get('animal')) #Gives output as 'None' when the value is not present in the dictionary
print(my_dict2.get('three'))  #Output: None, because there is no such value
print("\n")

#Clearing the dictionary - Eliminates all the key-value pair
print('CLearing the Dictionary:')
my_dict3 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2}
print(my_dict3)
my_dict3.clear()
print(my_dict3)
print('\n')

#ADDING NEW KEY-VALUE PAIR / NEW VALUE TO AN EXISTING KEY
print('Adding new value to the Dictionary:')
my_dict4 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2}
print(my_dict4)
my_dict4['three'] = 3     #Here, new key-value pair is created
print(my_dict4)
my_dict4['three'] = 57    #Here, the value is overwritten to that key

#PRINTING KEYS / VALUES / ITEMS OF THE DICTIONARY
print('Printing all the keys / values / items of the Dictionary:')
my_dict5 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2}
print(my_dict5)
print(my_dict5.keys())   #OUTPUT: dict_keys(['fruit', 'animal', 1, 'two'])
print(my_dict5.values()) #OUTPUT: dict_values(['apple', 'fox', 'one', 2])
print(my_dict5.items())  #OUTPUT: dict_items([('fruit', 'apple'), ('animal', 'fox'), (1, 'one'), ('two', 2)])  Here, thekey-value pairs are being displayed as a separate item.
print('\n')


#OPERATIONS:
'''
x={}
dir(x)

OUTPUT: clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update
'''

#COPYING A DICTIONARY
my_dict6 = my_dict5.copy()
print(id(my_dict6), id(my_dict5))   #Here, the memory location is not referenced and instead a new memory location is created
print(my_dict6)
print('\n')

#UPDATE A DICTIONARY WITH ANOTHER DICTIONARY
my_dict8 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2}  #OLD DICTIONARY
my_newdict = {'four': 4}   #NEW DICTIONARY
my_dict8.update(my_newdict)
print(my_dict8)
print('\n')

#POP - Provide the key to pop
print("POP - Provide the key to pop")
my_dict9 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2, "four": 4}
my_dict9.pop("four")
print(my_dict9)
print('\n')

#POPITEM - It Displays what it is removing, removes a random item
print('POPITEM - Removes a random item in the dictionary')
my_dict10 = {'fruit':'apple', 'animal':'fox', 1:'one', 'two': 2, "four": 4}
removed_item = my_dict10.popitem() #last item removed and is stored in var
print('Printing the removed item')
print(removed_item)
my_dict10.popitem()                #last item removed again
print(my_dict10)
print('\n')

#FROMKEYS
#creating a list of keys first
keys = ['a', 'e', 'i', 'o', 'u']
#creating a new dictionary with keys as aeiou
new_dict = dict.fromkeys(keys)
print(new_dict)
#updating the dictionary with whatever values you want
new_dict['a'] = "first alpha"
print(new_dict)

#SETDEFAULT - If there is no key in the dict, then it sets default key which you provide, if there's already a key, then it will not set as default
#No key present, hence sets default key
my_dict11 = {}
my_dict11.setdefault('k',45)
print(my_dict11)
#key present already, hence, it doesn't set it as default
my_dict11 = {'fruit':'apple'}
my_dict11.setdefault('fruit','orange')
print(my_dict11)

#