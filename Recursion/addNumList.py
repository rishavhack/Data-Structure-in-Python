def number(n):
	if len(n)==0:
		return 0
	else :
		return n[0] + number(n[1:])

print number([5,7,8,9])