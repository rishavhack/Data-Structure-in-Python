# importing  module calc.py
import calc
 
print add(10, 2)
# importing sqrt() and factorial from the 
# module math
from math import sqrt, factorial
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print sqrt(16)
print factorial(6)
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
 
# Sine of 2 radians
print math.sin(2) 
 
# Cosine of 0.5 radians
print math.cos(0.5) 
 
# Tangent of 0.23 radians
print math.tan(0.23)
 
# 1 * 2 * 3 * 4 = 24
print math.factorial(4) 