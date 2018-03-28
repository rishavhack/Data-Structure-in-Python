import itertools
import operator
li1=[1,4,5,7]
li2=[1,6,5,9]
li3=[8,10,5,4]

print "The sum after each iteration is :"
print list(itertools.accumulate(li1))
print "\n"
print "Multiplication  :"
print list(itertools.accumulate(li1,operator.mul))

print "Mentioned chain"
print list(itertools.chain(li1,li2,li3))