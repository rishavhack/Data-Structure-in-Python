# Python code to demonstrate difference between 
# Inplace and Normal operators in Immutable Targets
 
# importing operator to handle operator operations
import operator
x=5
y=6
a=5
b=6
z=operator.add(a,b)
p=operator.iadd(x,y)
print z
print p
print a
print x


print"\n"
#Mutable Targets
a=[1,2,3,4,5]
z=operator.add(a,[1,2,3])
print z

p=operator.iadd(a,[1,2,3])
print p