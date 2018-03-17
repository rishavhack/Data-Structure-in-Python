def bubble(a):
	for i in range(len(a)):
		for j in range(0,len(a)-i-1):
			if a[j] > a[j+1]:
				a[j],a[j+1] =a[j+1],a[j]

	return a
lst = range(5,99)
print bubble(lst)
