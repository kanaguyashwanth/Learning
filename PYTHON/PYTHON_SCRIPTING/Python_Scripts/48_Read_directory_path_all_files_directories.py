# READ A DIRECTORY PATH AND IDENTIFY ALL FILES AND DIRECTORIES
# THIS SCRIPT MENTIONS ALL THE FILES AND DIRECTORIES IN A PATH

import os
path = input("Enter your directory path: ")
file_dir_list = (os.listdir(path))           # THIS STORES IN THE FORM OF A LIST
print(file_dir_list)

path_1 = os.path.join(path, file_dir_list[0])
path_2 = os.path.join(path, file_dir_list[1])     # Path = Directory + File



# METHOD 1: Not the right way to find it because, it does not have the COMPLETE Path.
'''
import os
path = input("Enter your directory path: ")
file_dir_list = (os.listdir(path))           # THIS STORES IN THE FORM OF A LIST
print(file_dir_list)

path_1 = file_dir_list[0]
path_2 = file_dir_list[1]


# Checking for Path_1
if os.path.isfile(path_1):
    print(f"{path_1} is a file")
else:
    print(f"{path_1} is a directory")

# Checking for Path_2
if os.path.isfile(path_2):
    print(f"{path_2} is a file")
else:
    print(f"{path_2} is a directory")
'''

# METHOD 2: COMPLETE Path Method 
# Location: C:\Users\kyas\OneDrive - Hewlett Packard Enterprise\Desktop\Desktop\Python Scripts     
# File: Helloworld.py
# COMPLETE Path: C:\Users\kyas\OneDrive - Hewlett Packard Enterprise\Desktop\Desktop\Python Scripts\Helloworld.py      [JOINING THE LOCATION AND THE FILE]


