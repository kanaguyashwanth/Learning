import os
path = 'C:\\Users\\kyas\\OneDrive - Hewlett Packard Enterprise\\Desktop\\Desktop\\Python Scripts\\Python_Scripts\\test.py'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join(path))

#OUTPUT: After runnig this script   --->    We get, text.py as the output.

#Note:  Here, basename = test.py    ---> Ending part of C:\\Users\\kyas\\OneDrive - Hewlett Packard Enterprise\\Desktop\\Desktop\\Python Scripts\\Python_Scripts\\test.py
#             dirname = C:\\Users\\kyas\\OneDrive - Hewlett Packard Enterprise\\Desktop\\Desktop\\Python Scripts\\Python_Scripts
#                                   ---> Other than whichever part is there in the basename, that is called as Directory Name.

'''
Suppose,
PATH = C:\\Users\\kyas\\OneDrive
basename would be: OneDrive
dirname would be: C:\\Users\\kyas
'''



