def gcd(m,n):
	if m<n:
		(m,n)=(n,m)
	while m%n!=0:
		diff=m-n
		(m,n) = (max(n,diff),min(n,diff))
	return n


print gcd(29382,329323)