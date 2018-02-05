def Print(n):
	if n==0:
	    return 0;
	else:
		 print n
		 return Print(n-1)

print Print(8)