import random;
print "To import random number we use import random"
r1=random.random()
print "r1=random.random()->",r1
r2=random.choice([1,2,3,4,5,6,7,8,9])
print "r2=random.choice([1,2,3,4,5,6,7,8,9])",r2
r3=random.randint(1,1000)
print "r3=random.randamint(1,1000)->",r3
for i in range(10):
	ticket=random.randint(1,1000)
	print ticket
