def gcd(m,n):
	fm=[]
	for i in range(1,m+1):
		if m%i == 0:
			fm.append(i)

	fc=[]
	for i in range(1,n+1):
		if n%i==0:
			fc.append(i)

	fr=[]
	for f in fm:
		if f in fc:
			fr.append(f)

	return (fr[-1])


print gcd(21,27)