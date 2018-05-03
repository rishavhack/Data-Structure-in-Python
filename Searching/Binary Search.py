def binarySearch(arr,l,r,x):
	while l <= r:
		mid = l + (r -1)/2;
		if arr[mid]==x:
			return mid
		elif arr[mid]<x:
			l = mid +1
		else:
			r = mid-1

arr=[2,3,4,10,40]
x=10
print binarySearch(arr,0,len(arr)-1,x)