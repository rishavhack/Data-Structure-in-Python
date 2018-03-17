def SelectionSort(l):
	for start in range(len(l)):
		minpos = start
		print minpos
		for i in range(start,len(l)):
			if l[i] < l[minpos]:
				print i,minpos
				minpos=i
				(l[start],l[minpos])=(l[minpos],l[start])
	return l

lst = range(5,2,-1)
print SelectionSort(lst)