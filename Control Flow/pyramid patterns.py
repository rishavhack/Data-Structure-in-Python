#All code are for pyhton verison 3


def pypart(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print "*"
		print "\r"

print pypart(5)