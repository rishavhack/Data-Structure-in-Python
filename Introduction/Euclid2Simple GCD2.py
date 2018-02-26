def gcd(m,n):
	if m<n:
		(m,n)=(n,m)
	while (m%n)!=0:
		(m,n)=(n,m%n) #m%n < n alaways!
	return (n)