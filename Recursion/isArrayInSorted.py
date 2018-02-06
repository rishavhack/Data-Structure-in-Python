
def isArrayInSorted(n):
	if len(n)==1:
		return True
	else:
		return n[0]<n[1] and isArrayInSorted(n[1:]);

A=[2,3,5,4,6]
print isArrayInSorted(A)