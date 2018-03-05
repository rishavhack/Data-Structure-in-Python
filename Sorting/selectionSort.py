def SelectionSort(l):
	for start in range(len(l)):
		minpos = start
		for i in range(start,len(l)):
			if l[i] < l[minpos]:
				minpos=i
				(l[start],l[minpos])=(l[minpos],l[start])



