Day1 = [11,12,5,2] 
Day2 = [15,6,10] 
Day3 = [10,8,12,5] 
Day4 = [12,15,8,6] 
#The above data can be represented as a two dimensional array as below.
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print T[0]
print T[1][1]

for r in T:
	for c  in r:
		print c
	print "\n"