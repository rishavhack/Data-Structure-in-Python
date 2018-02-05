def sumOfNumber(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return n + sumOfNumber(n-1)




print sumOfNumber(5)