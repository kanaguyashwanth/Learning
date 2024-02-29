# sys.argv - One of the operation from the sys module.
#          - It returns a list of cmd line arguments passed to a python script
#          - Command line arguement example: python command_line.py hi how are you 12 3 4 ---> IS a CORRECT way as well, and is a cmd line argument.
#          - Inside the script, sys.argv captures the arguments that are being passed
#          - Index 0 - Always the script filename

'''
sys.argv - Captures the arguments that are being passed.
C:\Users\kyas\OneDrive - Hewlett Packard Enterprise\Desktop\Desktop\Python Scripts\Python_Scripts>python 40_command_line_argument.py i hello how are you 12 4 567 3
['40_command_line_argument.py', 'i', 'hello', 'how', 'are', 'you', '12', '4', '567', '3']
              |                  |      |       |      |      |     |     |     |     |
INDEX:        0                  1      2       3      4      5     6     7     8     9   
'''

#Note: Index 0 is always the script filename - 40_command_line_argument.py

