#base 2
s = "10010"
c = int(s,2)
print c
print '\n'
#Float .0
e = float(s)
print e
print '\n'
print "Character to integer of d ='4'"
d ='4'
c = ord(d)
print c
print '\n'
s = 16
print "Base 8 0f s= 16"
c = oct(s)
print c
print '\n'
print "Base 16 s = 16"
c = hex(s)
print c
print '\n'

s = 'Rishav'
print s
c = tuple(s)
print "Tuple Of Rishav: ",c
c=set(s)
print "Set of Rishav: ",c
c = list(s)
print "After Converting string to list:",c

#dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
a=1
b=2
tup = (('a', 1) ,('f', 2), ('g', 3))
print tup
c = complex(1,2)
print "Complex:: ",c
c = str(a)
print "Strr:",c
c=dict(tup)
print "dictionary: ",c