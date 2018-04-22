# IndexError, ImportError, IOError, ZeroDivisionError, TypeError.
# Python program to handle simple runtime error
 
a = [1, 2, 3]
try:
	print "Second element = %d"%(a[1])

	#Throw Error
	print "fourth element =%d" %(a[3])
except IndexError:
	print "An error occured"

print "\n"
try:
	a = 3
	if a<4:
		b = a/(a-3)

	print "Value of b =",b
except(ZeroDivisionError,NameError):
	print '\nError occured'

print "\n"
def AbyB(a,b):
	try:
		c = ((a+b)/(a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else: 
		print c

AbyB(2.0,3.0)
AbyB(3.0,3.0)

#Raising Exception:
print "\n"
try:
	raise NameError('Hi There')
except NameError:
	print "An Exception"
	raise