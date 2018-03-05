def sumofsquare(n):
	for i in range(1,n):
		for j in  range(1,n):
			if (i**2+j**2)==n:
				return True
	return False


print sumofsquare(41)
print sumofsquare(30)
print sumofsquare(17)