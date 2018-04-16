import functools
lis =[1,2,3,6,7,8]
print functools.reduce(lambda a,b : a+b,lis)
import operator
print functools.reduce(operator.add,lis)
print functools.reduce(operator.mul,lis)
