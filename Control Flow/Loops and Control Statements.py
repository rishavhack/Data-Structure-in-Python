count =0
while count<3:
	count=count+1;
	print "Hello Rishav"

print "\n"

print "List Iteration";
l = ["Rishav","for","you"]
for i in l:
	print i

print "\n";

print "Iteration over String"
s="Rishav";
for i in s:
	print i

print "\n";
print "Iteration Over Dictionary"
d=dict()
d['xyz']=123
d['abc']=345
for i in d:
	print "%s  %d" %(i,d[i])

print "\n"
for i in range(1,5):
	for j in range(i):
		print i
	print()

print "\n"
for letter in "Rishav":
	if letter == 'a' or letter =='s':
		continue
	print 'Current letter:',letter

print "\n"
for letter in "Rishav":
	pass
print 'Last letter',letter