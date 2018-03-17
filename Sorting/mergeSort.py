def mergesort(A,left,right):
	if right-left <=1:
		return(A[left:right])
	if right-left > 1:
		mid = (left+right)//2
		L = mergesort(A,left,mid)
		R = mergesort(A,mid,right)
		return (merge(L,R))

def merge(A,B):
	(C,m,n) = ([],len(A),len(B))
	(i,j)=(0,0)
	while i+j < m+n:
		if i==m:
			C.append(B[j])
		elif j==n:
			C.append(A[i])
		elif A[i] <= B[j]:
			C.append(A[i])
			i = i+1
		elif A[i] > B[j]:
			C.append(B[j])
			j = j+1
	return C

lst = list(range(10,1,-1))
print mergesort(lst,0,len(lst))

