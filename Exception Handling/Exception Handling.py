# IndexError, ImportError, IOError, ZeroDivisionError, TypeError.
# Python program to handle simple runtime error
 
a = [1, 2, 3]
try:
	print "Second element = %d"%(a[1])

	#Throw Error
	print "fourth element =%d" %(a[3])
except IndexError:
	print "An error occured"