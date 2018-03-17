x = int(input("Enter Any Number to find prime"));
if x == 1 or x==2 or x==3:
	print "It is Prime"
elif x>3:
	count = 0
	for i in range(2,x):
		if x%i==0:
			count += 1 
	if count != 1:
		print "It is prime"
	else:
		print "It is not prime"