x = int(input("Enter the number to which you find prime number"))
if x > 1:
	for i in range(2,x):
		if x%i==0:
			print "It is not prime"
			break;
	else:
		print x;