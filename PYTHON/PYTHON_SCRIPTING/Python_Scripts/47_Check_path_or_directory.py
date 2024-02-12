import os
path = input("Enter your path: ")

#First, we VERIFY if it is a valid path(Checking if it exists on the host or not) or not, then we check if that is a FILE PATH or DIRECTORY PATH
if os.path.exists(path):
    print(f"The given path: {path} is a valid path")
    if os.path.isfile(path):
        print(f"The given path: {path} is a File Path")
    else:
        print(f"The given path: {path} is a Directory Path")

else:
    print(f"The given file/direcotry: {path} does not exist on this host")