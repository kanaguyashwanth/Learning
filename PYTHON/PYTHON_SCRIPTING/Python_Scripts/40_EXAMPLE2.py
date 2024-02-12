#Note: RUN ONLY ON PYTHON TERMINAL!


#usr_str = input("Enter your string: ")
#usr_action = input("Enter action: [lower/upper/title] to the string: ")

#Note: Using sys.argv[] to eliminate 2 inputs

import sys
#Note: For this particular example, we need:  script_name.py  string  action
#There should be 3 total in the sys.argv list, if it is less/more than 3, then STOP the script

#To stop the sys if there are no sufficient arguments, DISPLAYS USAGE [Tells how to use]
if len(sys.argv) !=3:
    print(f'{sys.argv[0]} <your_req_string> <lower|upper|title>')
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]

#LOGIC
if (usr_action=="lower"):
    print(usr_str.lower())

elif (usr_action=="upper"):
    print(usr_str.upper())

elif (usr_action=="title"):
    print(usr_str.title())


