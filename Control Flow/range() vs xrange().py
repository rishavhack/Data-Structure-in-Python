a = range(1,800)
b = xrange(1,800)
print "The return type of range is",a
print "The return typeof xrange is",b

print "\n"
import sys

print "THe Size of range",sys.getsizeof(a)
print "the size of xrange",sys.getsizeof(b)