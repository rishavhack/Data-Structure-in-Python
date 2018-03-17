def appendAtBeginningFront(x,L):
    return [x + element for element in L]
def bitString(n):
	if n==0: 
		return[]
	if n==1:
		return["0","1"]
	else:
		return (appendAtBeginningFront("0",bitString(n-1)) + appendAtBeginningFront("1", bitString(n-1)) )


print bitString(8)