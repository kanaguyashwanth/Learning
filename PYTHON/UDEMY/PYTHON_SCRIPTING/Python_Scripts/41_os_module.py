#OS Modules are really crucial when it comes to automating taks at server site.
#OS Module - Used to work/interact iwth the OS to aumtomate many more tasks liek creating directory, remocving directory, identifying current directory and many more.

#For better understanding, let's divide OS Module into 4 parts
#   - os
#   - os.path
#   - os.system()
#   - os.walk()

'''
C:\Users\kyas\OneDrive - Hewlett Packard Enterprise\Desktop\Desktop\Python Scripts\Python_Scripts>
Here, the slash (\) is called OS Separator.
'''

'''
In the terminal, if we type:
import os
dir(os)     --->    Displays the functions and variables
help(os)    --->    We can see which are functions and which are vriables
'''

#Note: In WINDOWS, we have to provide the \\ instead of \ for the directory

#Note: Irrespective of the OS, python commands can be writtent to modify the directory of the OS

#Simple OS Operations:  ---> Irrespecitve of the OS, python commands can be used to change the directory of any OS unlike OS commands in each OS which is different
# os.sep
# os.getcwd()
# os.chdir(path)
# os.listdir()     ---> Wihtout path
# os.listdir(path) ---> With path
# os.mkdir(path)
# os.mkdirs("yashu/xyz/x")  ---> Recursive directory creation
# os.remove(path)
# os.removedirs(path)       ---> Recursive directory removal
# os.rmdir(path)
# os.rename(src, dst)
# os.environ
# os.getuid()     ---> User ID
# os.getpid()     ---> Process ID



