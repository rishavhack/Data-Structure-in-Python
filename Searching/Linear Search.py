def seaech(arr,x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1


arr = list(range(10))
print seaech(arr,3)
