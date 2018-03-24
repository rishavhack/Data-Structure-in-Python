#Using Nested List Comprehension:
print "Using Nested List Comprehension"
m = [[1,2],[3,4],[5,6]]
for row in m:
	print row
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print "\n"
print rez;
for row in rez:
	print row


#Using zip
print "UsingZip"
matrix =[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
	print row
print "\n"
t_matrix = zip(*matrix)
print t_matrix;
for row in t_matrix:
	print row

#Using numpy:
print "Using numpy"
import numpy
matrix=[[1,2,3],[4,5,6]]
print matrix
print "\n"
print (numpy.transpose(matrix))