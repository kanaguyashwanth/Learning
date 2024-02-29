# Write a single python script to clear terminal of any OS     /    Write a paltform independent script to clear any terminal

import os
import platform

if platform.system()=="Windows":
    os.system("cls")
else:
    os.system("clear")

