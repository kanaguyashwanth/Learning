# getpass() and getuser() modules:
'''
getpass() - prompts user for a password without echoing
          - secure way to handle the password prompts

getuser() - function that displays logn name of the user
          - checks env variabls like LOGNAME, USER, LNAME and USERNAME in order and returns value in non-empty string.

'''

import getpass
dir(getpass)


'''
TERMINAL:
>>> import getpass
>>> dir(getpass)
['GetPassWarning', '__all__', '__builtins__', 
 '__cached__', '__doc__', '__file__', 
 '__loader__', '__name__', '__package__', 
 '__spec__', '_raw_input', 'contextlib', 
 'fallback_getpass', 'getpass', 'getuser', 
 'io', 'msvcrt', 'os', 'sys', 'unix_getpass', 
 'warnings', 'win_getpass']
'''

