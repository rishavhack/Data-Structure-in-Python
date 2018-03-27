from collections import Counter

print Counter(['B','B','A','B','C','A','B','B','A','C'])
# With sequence of items 
print Counter(['B','B','A','B','C','A','B','B','A','C'])
 
# with dictionary
print Counter({'A':3, 'B':5, 'C':2})
 
# with keyword arguments
print Counter(A=3, B=5, C=2)

print "\n"
#Empty Counter
#coun = collections.Counter()
#Update krna ho
#coun.update(Data)
coun = Counter()
coun.update([1,2,3,1,2,1,1,2])
print coun
coun.update([1,2,4])
print coun
print "\n"

c1=Counter(a=4,b=3,c=10)
c2=Counter(a=10,b=3,c=4)
c1.subtract(c2)
print c1
print"\n"
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print Counter(z)
