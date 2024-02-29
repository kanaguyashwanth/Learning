
import mymodule
print(mymodule.value)

import math
print(math.pi)

#IMPORTING ALL PARAMTERES FROM math MODULE
from math import *
print(pi)
print(pow(4,2))

#IMPORTING PARTICULAR PARAMETERS FROM math MODULE
from math import pi, pow

#IMPORTING A MODULE IN ANOTHER NAME
import math as m
print(m.pi)

#IMPORT MODULES IN SAME LINE
import math, platform, sys, os, subprocess
'''
Instead of,
import math
import platform
import sys
import os
import subprocess
'''
