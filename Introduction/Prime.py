def isPrime(n):
	count = 0
	if n==2:
		return True
	else:
		for i in range(2,n):
			if n%i==0:
				count = count+1
		if count == 0:
			return True
		else:
			return False


print isPrime(75)
