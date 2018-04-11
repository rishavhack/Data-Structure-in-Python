# importing sqrt() and factorial from the 
# module math
from math import sqrt, factorial
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print sqrt(16)
print factorial(5)
import math
#  Import built-in module  random
import  random
print  dir(math)
# importing built-in module math
import math
 
# using square root(sqrt) function contained 
# in math module
print math.sqrt(25) 
 
# using pi function contained in math module
print math.pi 
 
# 2 radians = 114.59 degreees
print math.degrees(2) 
 
# 60 degrees = 1.04 radians
print math.radians(60) 
print "\n"
# Sine of 2 radians
print math.sin(90) 
 
# Cosine of 0.5 radians
print math.cos(0.5) 
 
# Tangent of 0.23 radians
print math.tan(0.23)
 
# 1 * 2 * 3 * 4 = 24
print math.factorial(4) 
import random
 
# printing random integer between 0 and 5
print random.randint(0, 5) 

# print random floating point number between 0 and 1
print random.random() 
print "\n"
# random number between 0 and 100
print random.random() * 100

List = [1, 4, True, 800, "python", 27, "hello"]
 
# using choice function in random module for choosing 
# a random element from a set such as a list
print random.choice(List)
 
 
# importing built in module datetime
import datetime
from datetime import date
import time
 
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print time.time() 