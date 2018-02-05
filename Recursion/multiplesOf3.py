def multipleOf3(n):
	if n == 0:
		return 0
	elif n==1:
		return 3
	else :
		return multipleOf3(n-1)+3



print multipleOf3(3)